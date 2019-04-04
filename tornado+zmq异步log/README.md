# zmq异步log

#### 功能介绍
使用tornado框架+zmq实现log异步输出，不影响业务本身的高并发性能

#### 软件架构
tornado+zmq+logging


#### 使用说明

1. logger_server为消费者utils.logger为生产者
2. 主项目中实例化生产者并绑定到application对象上(或其他对象)
3. 项目中要用到日志记录时先获取application对象(或其他对象)进而获取到生产者来进行日志记录
4. 项目日志的保存位置设置在settings中
5. 日志名字记录在logger_server中
6. 主项目日志端口和logger_server的端口要相同：define("logger_port", 8047, type=int)
7. 具体使用时建议搭配supervisor

