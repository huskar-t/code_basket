# 华为鲲鹏服务器安装docker-compose

### 华为鲲鹏服务器
华为鲲鹏服务器采用华为自研cpu ARMv8架构,提供 Windows 和多个Linux 系统，作为服务器使用我一直使用Centos系统(不会真有人用Ubuntu做生产环境吧？不会吧？不会吧？)。
本次使用 CentOS 7.6 64bit with ARM  

### 话不多说直接上脚本
不要问我为什么不用python2来安装docker-compose(我要是能安装成功还能去下载3吗？？？)
```shell script
#!/bin/bash
# 更新yum
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget http://mirrors.aliyun.com/repo/Centos-altarch-7.repo -O /etc/yum.repos.d/CentOS-Base.repo
yum makecache
# 安装docker
curl -fsSL https://get.daocloud.io/docker | bash -s docker --mirror Aliyun

# 配置docker
mkdir -p /etc/docker

tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://f1361db2.m.daocloud.io"],
  	"log-driver": "json-file",
	"log-opts": {
		"max-size": "50m",
		"max-file": "3"
	}
}
EOF

systemctl daemon-reload
systemctl restart docker

# docker-compose
yum install -y libffi libffi-devel openssl-devel python3 python3-pip python3-devel

pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple docker-compose
```