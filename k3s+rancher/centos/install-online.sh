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
    # centos7的内核经过k3s检查都有这个问题
    grubby --args="user_namespace.enable=1" --update-kernel="$(grubby --default-kernel)"
fi
# 添加加速源
sudo mkdir -p /etc/docker
tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://q0jtd7v2.mirror.aliyuncs.com"]
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
