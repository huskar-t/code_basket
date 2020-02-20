# k3s + rancher 实操
单机 k3s 和 rancher 操作、 k3s 集群  
已做自动脚本和离线镜像  
本文作为手动操作记录  
centos 7 以下内核符合要求  
Linux master 3.10.0-1062.9.1.el7.x86_64 #1 SMP Fri Dec 6 15:49:49 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
## 问题
>* micro 服务名不允许有下划线只能大驼峰
>* 安装之后运行 k3s check-config 血的教训,出现错误必须解决
>* 放弃centos8 提供的iptables版本太高！
>* 腾讯云 centos 默认主机名不符合k3s node 命名规范 ：指定 INSTALL_K3S_NAME 或修改 /etc/hostname 之后重启
>* worker 加入 master 失败时注意 K3S_TOKEN 是否正确 (cat /var/lib/rancher/k3s/server/node-token)
## 注意事项:
>* journalctl -u k3s 看k3s系统日志
>* 经测试腾讯云ubuntu 18.04正常
>* 阿里云单机导入 rancher的配置时 cattle-cluster-agent 网卡为 none CATTLE_SERVER 使用外网 ip 时无法连接,导入时 curl 获取配置使用内网 ip  
>* 腾讯云 centos 7.6 环境多次试验 k3s 无法启动 container 从 github 获取镜像手动导入也无效,估计是网络问题必要镜像没有拉取成功,待寻找国内镜像
## 分配swap
~~~bash
dd if=/dev/zero of=/var/swap bs=1024 count=8192000
mkswap /var/swap
mkswap -f /var/swap
swapon /var/swap
echo  "/var/swap swap swap defaults 0 0" >>  /etc/fstab

free -m
~~~
## 安装docker(centos 8)
~~~bash
curl https://download.docker.com/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
yum -y install https://download.docker.com/linux/fedora/30/x86_64/stable/Packages/containerd.io-1.2.6-3.3.fc30.x86_64.rpm

curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

sudo systemctl start docker
sudo systemctl enable docker

sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://q0jtd7v2.mirror.aliyuncs.com"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
~~~
## 安装rancher
~~~bash
docker run -d -v /data/docker/rancher-server/var/lib/rancher/:/var/lib/rancher/  --name rancher-server -p 80:80 -p 443:443 rancher/rancher:stable

##pause-amd64国内镜像
docker pull registry.cn-shanghai.aliyuncs.com/ilemonrain/pause-amd64:3.1
docker tag registry.cn-shanghai.aliyuncs.com/ilemonrain/pause-amd64:3.1 k8s.gcr.io/pause-amd64:3.1
~~~
## k3s离线安装

上传k3s
~~~bash
chmod 777 k3s
cp k3s /usr/local/bin/k3s
export INSTALL_K3S_SKIP_DOWNLOAD=true
export INSTALL_K3S_EXEC="--docker --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
curl -sfL https://get.k3s.io | sh -
~~~
有可能被墙多次执行 
~~~bash 
curl -sfL https://get.k3s.io | sh - 
~~~
## 问题排查命令
~~~bash
k3s kubectl get all --all-namespaces
kubectl describe pod cattle-cluster-agent-55d754f558-nldwz -n cattle-system

kubectl describe pod cattle-cluster-agent-55d754f558 -n cattle-system

kubectl logs -f cattle-cluster-agent-55d754f558-nldwz -n cattle-system

kubectl delete namespace cattle-system
~~~
pod id 随查询结果替换

## worker加入集群
server执行获取token
~~~bash
cat /var/lib/rancher/k3s/server/node-token
~~~
worke安装k3s-agent
~~~bash
cp k3s /usr/local/bin/k3s
export INSTALL_K3S_SKIP_DOWNLOAD=true
export K3S_URL=https://172.19.130.87:6443
export INSTALL_K3S_EXEC="--docker --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
export K3S_TOKEN=K102176f7836bd5b1de7cf1a81b30b1338962ffb8b7fa45e00b4a0c14c35885c9fc::server:f60b034156250b562b173c98bd9859d5
curl -sfL https://get.k3s.io | sh -
~~~
server查看
~~~bash
kubectl get nodes
~~~

## worker加入集群
server执行获取token
~~~bash
cat /var/lib/rancher/k3s/server/node-token
~~~
worker安装k3s-agent
~~~bash
cp k3s /usr/local/bin/k3s
export INSTALL_K3S_SKIP_DOWNLOAD=true
export K3S_URL=https://172.19.130.87:6443
export INSTALL_K3S_EXEC="--docker --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
export K3S_TOKEN=K102176f7836bd5b1de7cf1a81b30b1338962ffb8b7fa45e00b4a0c14c35885c9fc::server:f60b034156250b562b173c98bd9859d5
curl -sfL https://get.k3s.io | sh -
~~~

K3S_URL为server非本机
K3S_TOKEN为上一步获取的token

## 网络
外网选 NodePort --kube-apiserver-arg service-node-port-range=1000-65000启动参数指定了能暴露的端口范围
内网看情况选
无状态pod: {pod-ip}.{namespace}.pod.cluster.local
  例如某pod的ip为  1.2.3.4,在命名空间default与DNS名称cluster.local将有一个域名：1-2-3-4.default.pod.cluster.local
   
无状态pod: {hostname}.{subdomain}.{namespace}.svc.cluster.local
subdomain是在创建pod设定的属性,和hostname可以一起设置

有状态pod: pod名.服务名.命名空间.svc.cluster.local 或 pod名.服务名.命名空间
服务: 服务名.命名空间.svc.cluster.local 或 服务名.命名空间

无状态服务不需要获取pod的ip,获取到服务ip即为内部负载中的一个pod(负载均衡或只选取其中一个不确定)

使用hostport和nodeport无法ping通,直接使用即可
## 有状态服务
稳定、唯一的网络标识
稳定、持久的存储
按照顺序、优雅的部署和扩容
按照顺序、优雅的删除和终止
按照顺序、自动滚动更新
上述的稳定是持久的同义词，如果应用不需要稳定的标识或者顺序的部署、删除、扩容，则应该使用无状态的副本集。Deployment或者ReplicaSet的控制器更加适合无状态业务场景。

## 持久化存储 pv/pvc数据卷
~~~bash
#master节点安装nfs
yum -y install nfs-utils

#创建nfs目录
mkdir -p /nfs/data/

#修改权限
chmod -R 777 /nfs/data

#编辑export文件
vim /etc/exports
/nfs/data *(rw,no_root_squash,sync)

#配置生效
exportfs -r
#查看生效
exportfs

#启动rpcbind、nfs服务
systemctl restart rpcbind && systemctl enable rpcbind
systemctl restart nfs && systemctl enable nfs

#查看 RPC 服务的注册状况
rpcinfo -p localhost

#showmount测试
showmount -e 192.168.92.56

#所有node节点安装客户端
yum -y install nfs-utils
systemctl start nfs && systemctl enable nfs
~~~