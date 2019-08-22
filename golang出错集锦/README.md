# 花式出错

## 初始化问题

#### map
```go 
package main

import "fmt"

func main() {
	mapA := map[string]interface{}{}
	mapA["demoA"] = 11
	fmt.Println(mapA) //map[demoA:11]
	var mapB map[string]interface{}
	//未初始化mapB直接赋值
	mapB["demoB"] = 22
	fmt.Println(mapB) //panic: assignment to entry in nil map
}
```

## 奇怪的长度(初始化)
#### slice
```go
package main

import "fmt"

func main() {
	args := make([]int, 3)
	//初始化值
	for i := 0; i < 3; i++ {
		args = append(args, i)
	}
	fmt.Println("len args :",len(args),"args",args) //len args : 6 args [0 0 0 0 1 2]
//	make已经初始化了三个元素，之后再append直接在尾部插入

//	正确做法
	argsR := make([]int, 3)
	for i := 0; i < 3; i++ {
		argsR[i] = i
	}
	fmt.Println("len args :",len(argsR),"args",argsR) //len args : 3 args [0 1 2]
}

```
## 常见创建goroutine错误
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	c1 := make(chan int)

	go func() {
			select {
			case i := <-c1:
				fmt.Println("c1", i)
			}
	}()

	for {
	//想一直传值然后协程取值打印
		c1 <- 1
		time.Sleep(1 * time.Second)
	}
}
//输出
//c1 1
//fatal error: all goroutines are asleep - deadlock!

//创建的goroutine只有一次select所以c1只取一次值，当向c1第三次传值时死锁
//正确创建方法
//go func () {
//	for {
//		select {
//		case i := <-c1:
//			fmt.Println("c1", i)
//		}
//	}
//
//}()
```
## 定时任务
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	c1 := make(chan int)

	go func() {
		for{
			select {
			case i := <-c1:
				fmt.Println("c1", i)
			case <-time.After(time.Second * 2):
				fmt.Println(time.Now())
			}
		}
	}()

	for {
		c1 <- 1
		time.Sleep(1 * time.Second)
	}
}
//永远不会进到case <-time.After(time.Second * 2)执行fmt.Println(time.Now())打印当前时间
//只要在2秒内其他case执行了就不会触发<-time.After(time.Second * 2)
```
正确方法,创建time.Ticker对象,取Ticker.C
```go 
package main

import (
	"fmt"
	"time"
)

func main() {
	c1 := make(chan int)
	ticker := time.NewTicker(time.Second * 2)
	go func() {
		for {
			select {
			case i := <-c1:
				fmt.Println("c1", i)
			case <-ticker.C:
				fmt.Println(time.Now())
			}
		}
	}()

	for {
		c1 <- 1
		time.Sleep(1 * time.Second)
	}
}
```