package main
/*
#include <stdio.h>
void hello(){
	printf("Hello,Cgo!")
}
*/
import "C"
//C语言交互
//将c代码用/*,*/包含起来，紧挨着写import "C"即可, 不需要特别编译处理即可直接执行
//需要安装配置GCC
func Hello(){
	C.hello()
}
func main(){
	Hello()
}