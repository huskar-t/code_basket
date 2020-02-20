#!/bin/sh
set -e

#跨主机进行文件存取

#安装unzip
yum -y install unzip

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

#解压文件package文件夹内 config/  nginx/ client.zip
unzip -o -q package.zip -d /nfs/data
unzip -o -q -O UTF-8 /nfs/data/client.zip -d /nfs/data

#修改权限
chmod -R 777 /nfs/data
echo 'finish'
echo "$(ifconfig eth0 |grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:")"