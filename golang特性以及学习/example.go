package main

import (
	"fmt"
	"math/rand"
	"runtime"
)

func demo(){
	var myMap map[string]string // 字典声名，声明的map是空值，需要用make()创建
	myMap = make(map[string]string) //必须用make分配空间否则就是nil,无法对map赋值
	_ = myMap
}

func add(x int,y int) int{   // 这里也可以写成add(x,y int)
	return x + y
}

// 函数内声明的变量必须被使用,否则会报错
func nouse(){
	var no string
	// 变量未使用报错
	// 可以使用'_ = no'来避免报错
	_ = no
}

// 可以是空函数体
func empty(){
}

// 可变参数
func vary(args... int) {
	fmt.Println(args)
}
// vary()       -> [] 可以为空
// vary(1)      -> [1]
// vary(1,2,3)  -> [1 2 3]

// 混合使用固定参数与可变参数，可变参数放在最后，不能与固定参数共用参数类型
func fix_vary(fix int, args...int) {  // fix可以不使用
	fmt.Println(args)
}

// 多值返回, 这个函数可以直接用多重赋值实现x,y = y,x
func swap(x, y int) (int,int){
	return y, x
}

// 返回值指定变量名
func split(sum int) (x,y int) {
	x = sum / 5
	y = sum % 5
	return  // 当指定变量名时，返回可以略去不写
}

func lambda(){
	// 匿名函数
	//func(x,y int)int{
	//	return x+y
	//}
	// 匿名函数直接执行, 直接在函数定义后面加上参数即可
	func(x,y int)int{
		return x+y
	}(2,3)  // 传入参数2,3运行
	// 匿名函数赋值
	f := func(x,y int)int{
		return x+y
	}
	_=f
}

//switch,case,select
func demo2(){
	i:=1
	switch i {
	case 0:
		// ...
	case 1:
		// ...
		// ...
	default:
		// ...
	}
	// switch后面的表达式不是必须的
	seed := rand.Intn(1)
	chars := []byte{'a','b'}
	char := chars[seed]
	switch{
	case char == 'a':
		// ...
	case char == 'b':
		// ...
	}
	// 单个case可出现多个可选结果
	switch 1 {
	case 1,2,3:
		// ...
	default:
		// ...
	}
	// 可以初始化变量,可以不做任何处理
	switch os:=runtime.GOOS;os{
	case "darwin":
	case "linux":
	}
}
