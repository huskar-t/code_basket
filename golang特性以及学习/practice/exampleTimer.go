package main

import (
	"fmt"
	"time"
)

func main() {
	timer1 := time.NewTimer(time.Second*2)
	go func() {
		<-timer1.C
		fmt.Println("time1 expired")
	}()
	time2 := time.NewTimer(time.Second)
	go func(){
		<-time2.C
		fmt.Println("time2 expired")
	}()
	stop2 := time2.Stop()
	if stop2{
		fmt.Println("time2 stopped")
	}
}
