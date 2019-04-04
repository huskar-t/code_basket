# beego框架搭建

#### beego介绍
基于golang的MVC框架
github: github.com/astaxie/beego

#### 安装
1. beego安装参照https://beego.me/docs/install/
2. bee工具安装参照https://beego.me/docs/install/bee.md

#### bee介绍
搭配beego的工具

#### bee命令
1. version : 显示bee、beego、golang版本
2. migrate : 数据库升降级
3. api : 创建基于beego的api应用
4. bale : 将资源文件同时打包进二进制文件（*不完善，不要使用*）
5. new : 创建beego应用
6. run : 启动beego应用，热编译
7. pack : 打包项目(参数可设置跨平台编译)
8. fix : 修复项目以适应最新的beego
9. dlv : 用Delve调试项目
10. dockerize : 为项目生成Dockerfile
11. generate : 通过已存在数据库生成go代码
12. hprose : 使用hprose和beego创建rpc应用