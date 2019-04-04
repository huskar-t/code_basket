# tornado框架的服务端webSocket用例及网络异常时解决方案

#### 功能介绍
使用tornado结合实际项目经验写的简单例子

#### 使用说明

handler.py为webSocket具体使用
session_manager.py为每个webSocket连接对象的管理
example_main.py为项目入口

#### 具体说明
tornado提供WebSocketHandler，在具体实现中只需要重写open(连接)、on_message(接收消息)、on_close(断开连接)这三个方法，
而不用关心如握手等具体的实现细节，然而在实际项目中由于客户端-服务端实时连接并不完全可靠，所以有可能出现连接异常情况，
这种情况出现在客户端突然关闭网络连接或客户端的网络信号弱和服务端断开连接，而服务端无法得知这种情况发生，所以采用心跳
的方式来进行这种情况的处理。
1. 由tornado框架提供的PeriodicCallback方法进行定时循环任务进行心跳检测
2. 为webSocket添加更新时间属性
3. 在open方法在session_manager中进行webSocket连接对象注册
4. 在每次获取到客户端消息时刷新更新时间
5. 在每次心跳检测时对所有webSocket对象进行更新时间检测
6. 对于超时的连接进行反注册同时关闭连接