package main

import (
	"fmt"
	"math/rand"
	"sync/atomic"
	"time"
)

//有状态goroutine

type readOp struct {
	key  int
	resp chan int
}
type writeOp struct {
	key  int
	val  int
	resp chan bool
}
//这个示例主要是利用select来保证每次只有一个goroutine操作state字典
//写任务将id和状态写到state，返回true
//读任务从state读出状态，返回状态
//注意一点：map取不存在的键会返回值的默认空值
func main() {
	var readOps uint64 = 0
	var writeOps uint64 = 0
	reads := make(chan *readOp)
	writes := make(chan *writeOp)
	go func() {
		var state = make(map[int]int)
		for {
			select {
			case read := <-reads:
				read.resp <- state[read.key]
			case write := <-writes:
				state[write.key] = write.val
				write.resp <- true
			}
		}
	}()
	for r := 0; r < 100; r++ {
		go func() {
			for {
				read := &readOp{
					key:  rand.Intn(5),
					resp: make(chan int),
				}
				reads <- read
				<-read.resp
				atomic.AddUint64(&readOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}
	for w := 0; w < 10; w++ {
		go func() {
			for {
				write := &writeOp{
					key:  rand.Intn(5),
					val:  rand.Intn(100),
					resp: make(chan bool),
				}
				writes <- write
				<-write.resp
				atomic.AddUint64(&writeOps, 1)
				time.Sleep(time.Millisecond)
			}
		}()
	}
	time.Sleep(time.Second)
	readOpsFinal := atomic.LoadUint64(&readOps)
	writeOpsFinal := atomic.LoadUint64(&writeOps)
	fmt.Println("readOps:", readOpsFinal)
	fmt.Println("writeOps:", writeOpsFinal)
}
