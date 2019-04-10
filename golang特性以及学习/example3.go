package main

import (
	"fmt"
	"runtime"
	"sync"
)

//并发
//关键字go简单暴力实现并发，不同于线程/进程，更轻量级的协程
func Add(x, y int) {
	z := x + y
	fmt.Println(z)
}
func main_go() {
	for i := 0; i < 10; i++ {
		go Add(i, i)
	}
}

//并发通信
//互斥锁方法
var counter int = 0

func Count(lock *sync.Mutex) {
	lock.Lock()
	counter++
	fmt.Println(counter)
	lock.Unlock()
}
func syncMain() {
	lock := &sync.Mutex{}
	for i := 0; i < 10; i++ {
		go Count(lock)
	}
	for {
		lock.Lock()
		c := counter
		lock.Unlock()
		runtime.Gosched()
		if c >= 10 {
			break
		}
	}
}

//channel实现并发通信
func CountChannel(ch chan int) {
	ch <- 1
	fmt.Println("counting")
}
func channelMain() {
	chs := make([]chan int, 10)
	for i := 0; i < 10; i++ {
		chs[i] = make(chan int)
		go CountChannel(chs[i])
	}
	for _, ch := range (chs) {
		<-ch //这里是读出数据，如果数据不读取会阻塞其他协程写入数据
	}
}

//channel
//chan与map类似，没有make时是不能使用的，所以声明与make最好一起
func demoChannel() {
	var ch1 chan int
	var ch2 chan<- float64 //单向通道，只用于写float64数据
	var ch3 <-chan int     //单向通道，只用于读int数据
	_, _, _ = ch1, ch2, ch3
	ch := make(chan int) //不带缓冲的channel,如果ch中没数据则读取会被阻塞，如果ch中有数据则写入会被阻塞
	go func() {
		ch <- 1
	}()
	i := <-ch     // 取数据并使用
	<-ch          // 取数据但不使用，这个位置死锁
	x, ok := <-ch //ok标识有没有取到数据，与类型判断与map取值类似
	_, _, _ = x, i, ok
	//带缓冲的channel
	chbuf := make(chan int, 100) // 没有数据时读取阻塞，数据满100个时阻塞写入
	_ = chbuf

}

//单向通道
//单向通道一般用于函数参数定义
func single_r(ch <-chan int) {
	//只能读
}
func single_w(ch chan<- int) {
	//	只能写
}
func demoChannelSingle() {
	var ch chan int //定义双向通道
	single_r(ch)    //只读
	single_w(ch)    //只写
}

//select，与switch类似，但是是专用多通道读取
func demoSelect() {
	var chan1 = make(chan int)
	var chan2 = make(chan int)
LOOP:
	for {
		select {
		case <-chan1:
			//如果chan1读到数据，则进行case处理
			//dosth
		case <-chan2:
			//如果chan2读到数据则退出Loop
			break LOOP
		default:
			//	如果上面都没成功，则进入defalut处理
			//一般用 <- time.After(duration)替代default做读写默认超时处理
		}
	}
	//读取某个chan中所有数据
	var ch = make(chan int)
	for i := range ch {
		_ = i
		//	dosth
	}
}

//通道经常使用的特殊数据：
//chan <- struct{}{}
//语义为将一个空数据传递给channel.因为struct{}{}占用的内存非常小，而且我们对数据内容也不关心,通常用来做信号量来处理

//异常处理
//panic defer recover

// 当在一个函数执行过程中调用panic()函数时,正常的函数执行流程将立终止,
// 但函数中之前使用defer关键字延迟执行的语句将正常展开执行，然后返回到调用函数，逐层向上执行panic，
// 直到所属的goroutine中所有正在执行的函数被终止
//recover()函数用来终止panic流程，放在defer关键词后面的函数中执行
func demoPanic() {
	defer func() {
		if err := recover(); err != nil {
			// 处理错误
		}
	}()

	// ...

	panic("something error") // 这个panic将被上面的defer捕获，阻止程序退出
}

