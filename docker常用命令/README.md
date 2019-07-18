#docker常用命令

##pune

```cmd
删除所有未被容器使用的镜像:
docker image prune -a

删除所有停止运行的容器:
docker container prune

删除所有未被挂载的卷:
docker volume prune

删除所有网络:
docker network prune

删除 docker 所有资源:
docker system prune
```

##批量命令
```cmd
停止所有包含test-的容器:
docker ps -a | grep "test-" | awk '{print $1 }'|xargs docker stop

删除所有包含test-的镜像:
docker images|grep "test-"|awk '{print $3 }'|xargs docker rmi
```