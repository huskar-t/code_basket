## 当前路径下的Dockerfile生成镜像
docker build -t client .
## 复制到镜像的文件权限
与外部一直,应在外部设置好权限后用ADD或COPY,如果添加进去之后再使用RUN chomd 命令会增加一层使镜像变大。

## Dockerfile 命令
> * FROM 指定基础镜像
> * RUN 运行制定命令
> * CMD 容器启动时要运行的命令
> * LABEL 为镜像指定标签
> * MAINTAINER 指定作者
> * EXPOSE 暴露端口
> * ENV 设置环境变量
> * ADD 复制文件到镜像
> * COPY 复制文件到镜像
> * ENTRYPOINT 启动时默认命令，只能写一条命令
> * VOLUME 将外部文件夹挂载到这个容器
> * USER 设置启动容器的用户，可以是用户名或UID只有下面的两种写法是正确的   
> >* USER daemo  
> >* USER UID
> * WORKDIR 设置工作目录，对RUN,CMD,ENTRYPOINT,COPY,ADD生效。如果不存在则会创建，也可以设置多次。 
> * ARG 设置变量命令，在docker build创建镜像的时候，使用 --build-arg <varname>=<value>来指定参数，如果用户在build镜像时指定了一个参数没有定义在Dockerfile种，那么将有一个Warning
> * ONBUILD 后接命令，该命令只对当前镜像的子镜像生效
> * STOPSIGNAL 当容器退出时给系统发送的命令
> * HEALTHCHECK 容器健康状态检查
