##[使用portainer管理](../portainer)
##使用镜像
docker pull consul
##生成唯一id
uuidgen | awk '{print tolower($0)}'
##-bootstrap-expect=3 三个节点后产生leader
agent -server -bind=172.10.0.2 -bootstrap-expect=3 -node=node1

agent -server -bind=172.10.0.3  -join=172.10.0.2 -node-id=9bf8292c-2e8f-418c-ab36-30cc90c34992  -node=node2
##-client=172.10.0.4 对外clientIp对另外机器上的服务注册使用，不设置则为本机无法给别的机器上提供服务
agent -server -bind=172.10.0.4  -join=172.10.0.2 -node-id=5239d1e8-1115-415d-8cd6-3d975cea0c74  -node=node3 -client=172.10.0.4

##仅启动客户端
agent -bind=172.10.0.5 -retry-join=172.10.0.2 -node-id=c2574c40-32a7-4952-b1b8-d8fc1e070986  -node=node4
##对外提供ui界面
agent -server -bind=172.10.0.6  -join=172.10.0.2 -node-id=9f002297-5863-4987-9e87-30f8858d758c  -node=node5 -client 0.0.0.0 -ui