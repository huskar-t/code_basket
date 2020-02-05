# k3s + rancher 实操
单机 k3s 和 rancher 操作
## 注意事项:
阿里云单机导入 rancher的配置时 cattle-cluster-agent 网卡为 none CATTLE_SERVER 使用外网 ip 时无法连接,导入时 curl 获取配置使用内网 ip
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