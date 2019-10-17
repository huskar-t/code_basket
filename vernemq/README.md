# vernemq
开源mqtt服务端

###特点
开源，Apache2.0协议，erlang编写方便分布式，提供docker镜像，性能中等

###部署
1. docker部署:  
    默认不支持匿名连接需设置环境变量DOCKER_VERNEMQ_USER_用户名=密码
    1. bridge网络
        ```bash
        docker run -p 1883:1883 -e DOCKER_VERNEMQ_USER_admin=password --name vernemq1 -d erlio/docker-vernemq
        ```
    2. host网络
       ```bash
        docker run --net host -e DOCKER_VERNEMQ_USER_admin=password --name vernemq1 -d erlio/docker-vernemq
        ```
2. linux裸机安装:  
    https://vernemq.com/downloads/index.html  
    下载对应的安装包进行安装

###设置
    配置文件:
    /etc/vernemq/vernemq.conf
    裸机绑定127.0.0.1
    docker bridge网络绑定bridge分配的网卡,host模式绑定外网网卡(如果有外网网卡则用127.0.0.1无法连接上)
mqtt默认配置  
listener.tcp.default = 127.0.0.1:1883  
listener.ws.default = 127.0.0.1:8888

添加自定义配置  
listener.tcp.my_other = 127.0.0.1:18884
listener.tcp.my_other.max_connections = 100

###加入集群
    docker创建容器时添加参数
    -e "DOCKER_VERNEMQ_DISCOVERY_NODE=<IP-OF-VERNEMQ1>"