# golang数据聚合的优雅操作

## 场景：
需要将上传的数据进行特性分组之后再进行数据库**批量**插入或流向下一个处理方法。
## 痛点：
由于数据不确定性做聚合操作之后会有多组数据需要缓存，如果多协程进行操作需要将缓存数据进行加锁，容易造成数据死锁。
## 解决：
通过管道和select进行数据传递，同时在select中做缓存的所有操作，在给定条件流向下一个处理方法时通过channel传递过去同时清空对应缓存，
这样操作都在select中不会有竞争发生。
## 具体方法：
1.创建缓存  
2.创建select处理缓存数据流过来的通道  
3.在select中缓存数据同时聚合数据，之后判断是否流向下一通道  
4.创建worker处理聚合后数据

## 样例

```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

type Data struct {
	Id    int
	Value interface{}
}

func main() {
	execCacheCount := 50
	workerCount := 10
	c := make(chan Data)
	stream := make(chan map[int][]Data)
	go func() {
		cache := map[int][]Data{}
		for {
			select {
			case data := <-c:
				cacheData, exist := cache[data.Id]
				if exist {
					cacheData = append(cacheData, data)
				} else {
					cacheData = []Data{data}
				}
				cache[data.Id] = cacheData
				if len(cacheData) >= execCacheCount {
					stream <- cache
					cache = map[int][]Data{}
				}
			}
		}
	}()

	for i := 0; i < workerCount; i++ {
		go func() {
			for {
				select {
				case data := <-stream:
					for key, value := range data {
						fmt.Println("key:", key, "values:", value)
					}
				}
			}
		}()
	}
	for {
		r := rand.New(rand.NewSource(time.Now().UnixNano()))
		data := Data{
			Id:    r.Intn(10),
			Value: r.Intn(20),
		}
		c <- data
		time.Sleep(20 * time.Millisecond)
	}
}
```
