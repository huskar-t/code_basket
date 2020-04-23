# 华为鲲鹏服务器安装 k3s+rancher

## 华为鲲鹏服务器
华为鲲鹏服务器采用华为自研cpu ARMv8架构,提供 Windows 和多个Linux 系统，作为服务器使用我一直使用Centos系统(不会真有人用Ubuntu做生产环境吧？不会吧？不会吧？)。
本次使用 CentOS 7.6 64bit with ARM  
为什么不用 CentOS 8.0 ? 看我之前的文章吧

## 安装docker
使用阿里云的仓库安装或者直接使用脚本安装
```shell script
# 更新yum
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
wget http://mirrors.aliyun.com/repo/Centos-altarch-7.repo -O /etc/yum.repos.d/CentOS-Base.repo

# 安装docker
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun

sudo systemctl start docker
sudo systemctl enable docker
```
注意阿里云仓库地址中的 `Centos-altarch-7`这个是arm64的仓库
`https://get.docker.com` 脚本可能无法下载
可以替换为`https://get.daocloud.io/docker`

## 配置镜像加速器
可以使用阿里云,华为云和daocloud  
使用方法都一样改`registry-mirrors`为对应的加速地址
~~~shell script
sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["http://f1361db2.m.daocloud.io"]
}
EOF

sudo systemctl daemon-reload
sudo systemctl restart docker
~~~

### 改一个配置
k3s check-config 显示 user_namespace 未启用
```shell script
grubby --args="user_namespace.enable=1" --update-kernel="$(grubby --default-kernel)"
```
重启之后生效

### 安装k3s脚本
```shell script
export K3S_NODE_NAME=iot001
export INSTALL_K3S_EXEC="--docker --write-kubeconfig ~/.kube/config --write-kubeconfig-mode 666"
curl -sfL https://docs.rancher.cn/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```
`K3S_NODE_NAME`这个最好自己指定使用系统名会产生各种不兼容比如:中划线

### 安装nfs客户端
```shell script
#所有node节点安装nfs客户端
yum -y install nfs-utils
systemctl start nfs && systemctl enable nfs
```

### 安装rancher
```shell script
#rancher
docker run -d -v /data/docker/rancher-server/var/lib/rancher/:/var/lib/rancher/ --restart=unless-stopped --name rancher-server -p 9443:443 rancher/rancher:v2.4.2-linux-arm64

echo https://$(curl http://ip.cip.cc/):9443
```
### rancher 导入 k3s 
见我之前的文章

### 产生的问题
> * docker、k3s和rancher都支持arm64上运行,但是rancher提供的监控以及应用商店里面的镜像大部分不支持arm64运行
> * 应用程序使用upx压缩之后在arm64平台无法运行,docker内也无法运行。可以使用在2020-01-23日更新的3.96版本upx进行压缩(快两年终于更新了)
> * 不兼容问题：代表作redis ,redis镜像虽然支持arm64但是CentOS分页大小64kb,主流Linux分页4kb,然后启动的时候崩了(CentOS倒了呜呜呜)。  
解决办法：在鲲鹏CentOS系统拉取Redis仓库重新构建镜像(选香港机器构建具体原因大家懂得,如果需要编译好的镜像可以私信我)

### 总结
> * 鲲鹏服务器使用自研arm64 cpu 堪称国产之光，然而现在x86市场占据主流的情况下应用程序有arm64版本的太少了。如果是想迁移到鲲鹏服务器进行生产任务一定要看清楚所依赖的软件是不是有arm64版本的
> * 现阶段不推荐使用k3s+rancher的方式在鲲鹏服务器进行业务部署，但是可以单独使用k3s+自定义配置文件方式进行业务部署。推荐等后续rancher对arm架构更好的优化，应用市场arm架构镜像达到一定数量的时候再使用
> * golang大法好