# protobuf使用

#### 功能介绍
Google protobuf python使用

#### 使用说明
protocol buffers 是一种语言无关、平台无关、可扩展的序列化结构数据的方法，它可用于（数据）通信协议、数据存储等。
Protocol Buffers 是一种灵活，高效，自动化机制的结构数据序列化方法－可类比 XML，但是比 XML 更小（3 ~ 10倍）、更快（20 ~ 100倍）、更为简单。
你可以定义数据的结构，然后使用特殊生成的源代码轻松的在各种数据流中使用各种语言进行编写和读取结构数据。你甚至可以更新数据结构，而不破坏由旧数据结构编译的已部署程序。

项目中主要为了在多平台使用，减小传输包体积同时有一定的加密能力
需要protobuf包
1. 编写proto文件
2. Google官方工具生成对应python文件
3. 序列化方法SerializeToString()
4. 反序列化方法ParseFromString([protobuf_string])

