# Portainer安装使用

### 简介
    Portainer 是轻量级docker管理工具由web页面控制
    
#### 使用
    docker run -d -p 9000:9000 --restart=always -v /var/run/docker.sock:/var/run/docker.sock --name portainer  docker.io/portainer/portainer