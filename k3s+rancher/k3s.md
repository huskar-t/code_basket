
- [K8S ? K3S ！](#k8s--k3s-)
    - [K3S](#k3s)
    - [踩坑开始](#踩坑开始)
        - [歪比歪比(奇怪的服务器)](#歪比歪比奇怪的服务器)
            - [服务器选择我熟悉的 **Centos**](#服务器选择我熟悉的-centos)
            - [K3S内置 **Containerd** 但是！作为一个服务器使用自然是要用常见的一点的容器 **Docker**](#k3s内置-containerd-但是作为一个服务器使用自然是要用常见的一点的容器-docker)
        - [歪比巴卜(K3S 的胜利)](#歪比巴卜k3s-的胜利)
            - [K3S Server 安装](#k3s-server-安装)
            - [安装 nfs](#安装-nfs)
            - [K3S Server 信息](#k3s-server-信息)
            - [K3S agent](#k3s-agent)
        - [一大波僵尸即将来袭( rancher 安装)](#一大波僵尸即将来袭-rancher-安装)
    - [Docker + K3S + nfs 客户端 一键安装脚本](#docker--k3s--nfs-客户端-一键安装脚本)

# K8S ? K3S ！
K8S 那么麻烦为什么不用 K3S？  
本文适合 :
> * 想摆脱 K8S 复杂安装又不得不用 K8S 的开发者
> * 服务器配置不够跑 K8S 的开发者
> * 物联网开发者
> * 需要最低学习成本使用容器编排的开发者
> * 初学 K8S 的新手

## K3S
* 更轻、更简单的 K8S  
* 设计给物联网设备和边缘侧计算使用  
* 边缘侧都能用服务器用了还不直接起飞？- 鲁迅

## 踩坑开始

### 歪比歪比(奇怪的服务器)

#### 服务器选择我熟悉的 **Centos**
> 内核要求: 3.10.0 也就是阿里云和腾讯云的官方 Centos7.7 / Centos7.6
> 1. Centos8 不用尝试了 iptables 的版本太高
> 2. 其他内核使用前用 ```k3s check-config``` 命令检查
> 3. 所有节点机器要在同一个内网环境下,这是K3S的一个bug,集群会以 endpoint 进行连接,而云服务器的 endpoint 是内网ip(阿里云经典网络应该不是 暂未测试)
> 4. 主机名带下划线在 k3s 异常
>   ```shell script 
>   export K3S_NODE_NAME=${HOSTNAME//_/-}
>   ``` 
>   将下划线替换成中划线提供给 k3s 安装脚本

#### K3S内置 **Containerd** 但是！作为一个服务器使用自然是要用常见的一点的容器 **Docker**  
> ```
> curl https://download.daocloud.io/docker/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
> curl -fsSL https://get.daocloud.io/docker | bash -s docker --mirror Aliyun
> ```
> * Docker 安装和配置加速器(国内源):
>  + containerd.io 版本低:
>```
>yum -y install https://download.daocloud.io/docker/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
>```
>  + 加速器配置:
>   ```shell script
>   sudo mkdir -p /etc/docker
>   tee /etc/docker/daemon.json <<-'EOF'
>   {
>     "registry-mirrors": ["http://f1361db2.m.daocloud.io"]
>   }
>   EOF
>   sudo systemctl daemon-reload
>   sudo systemctl restart docker
>   ```
> * 开机启动
>  ```shell script
>  sudo systemctl enable docker
>  ```

### 歪比巴卜(K3S 的胜利)

#### K3S Server 安装
就这么写！都是一点一点查到的经验！
```shell script
export K3S_NODE_NAME=${HOSTNAME//_/-}
export INSTALL_K3S_EXEC="--docker --kube-apiserver-arg service-node-port-range=1-65000 --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
curl -sfL https://docs.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```
> * ```--docker```使用docker  
> * ```--kube-apiserver-arg service-node-port-range=1-65000```节点端口范围1-65000  
> * ```--no-deploy traefik```不安装traefik (后续用 rancher )
> * ```--write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666```设置kube配置文件到```~/.kube/config```(和 k8s 路径一致后续会少出问题)

#### 安装 nfs
所有机器：
```shell script
#所有 node 节点安装 nfs 客户端
yum -y install nfs-utils
systemctl start nfs && systemctl enable nfs
```
nfs主机：
```shell script
#master节点安装nfs
yum -y install nfs-utils

#创建nfs目录
mkdir -p /nfs/data/

#修改权限
chmod -R 777 /nfs/data

#编辑export文件
tee /etc/exports <<-'EOF'
/nfs/data *(rw,no_root_squash,sync)
EOF

#配置生效
exportfs -r

#启动rpcbind、nfs服务
systemctl restart rpcbind && systemctl enable rpcbind
systemctl restart nfs && systemctl enable nfs
```

#### K3S Server 信息
agent 加入集群需要使用
```shell script
echo "export K3S_TOKEN=$(cat /var/lib/rancher/k3s/server/node-token)"
echo "export K3S_URL=https://$(ifconfig eth0 |grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"):6443"
```

#### K3S agent
同 server 安装参数，需要先获取到 server 的 K3S_TOKEN 和 K3S_URL
```shell script
export K3S_TOKEN=XXXXXX
export K3S_URL=XXXXXX
export K3S_NODE_NAME=${HOSTNAME//_/-}
export INSTALL_K3S_EXEC="--docker --kube-apiserver-arg service-node-port-range=1-65000 --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
curl -sfL https://docs.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```

### 一大波僵尸即将来袭( rancher 安装)
rancher 版本: ***Rancher2.3+***
```shell script
docker run -d -v /data/docker/rancher-server/var/lib/rancher/:/var/lib/rancher/ --restart=unless-stopped --name rancher-server -p 9443:443 rancher/rancher:stable
echo https://$(curl http://ip.cip.cc/):9443
```
> * 主机 9443 端口代理 rancher https 使用的 443 端口
> * rancher 界面直接导入 K3S 集群, 把 K3S 集群当成 K8S 使用

## Docker + K3S + nfs 客户端 一键安装脚本
```shell script
#!/bin/sh
set -e
# 在线安装脚本

# k3s 不建议安装swap 系统内存小的时候没有swap会卡死
if [ ! -f "/var/swap" ];then
    echo "create swap"
    dd if=/dev/zero of=/var/swap bs=1024 count=8192000
    mkswap /var/swap
    mkswap -f /var/swap
    swapon /var/swap
    echo  "/var/swap swap swap defaults 0 0" >>  /etc/fstab
fi

# 判断是否安装 docker
if [ `command -v docker` ];then
    echo 'docker has installed'
else
    echo 'install docker'
    curl https://download.daocloud.io/docker/linux/centos/docker-ce.repo -o /etc/yum.repos.d/docker-ce.repo
    yum -y install https://download.daocloud.io/docker/linux/centos/7/x86_64/stable/Packages/containerd.io-1.2.6-3.3.el7.x86_64.rpm
    curl -fsSL https://get.daocloud.io/docker | bash -s docker --mirror Aliyun
    # centos7 的内核经过 k3s 检查都有这个问题
    grubby --args="user_namespace.enable=1" --update-kernel="$(grubby --default-kernel)"
fi
# 添加加速源
sudo mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://f1361db2.m.daocloud.io"]
}
EOF
# 启动
sudo systemctl daemon-reload
sudo systemctl restart docker
sudo systemctl enable docker

# 判断是否安装k3s
if [ `command -v k3s` ];then
    echo 'k3s has installed'
else
    # 本地安装k3s其他参数通过外部传入
    # 下划线节点名不被支持
    export K3S_NODE_NAME=${HOSTNAME//_/-}
    export INSTALL_K3S_EXEC="--docker --kube-apiserver-arg service-node-port-range=1-65000 --no-deploy traefik --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
    curl -sfL https://docs.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
fi

#所有node节点安装nfs客户端
yum -y install nfs-utils
systemctl start nfs && systemctl enable nfs
echo 'finish'
echo 'need reboot'
echo "export K3S_TOKEN=$(cat /var/lib/rancher/k3s/server/node-token)"
echo "export K3S_URL=https://$(ifconfig eth0 |grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"):6443"
```