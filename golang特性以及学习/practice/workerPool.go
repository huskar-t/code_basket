package main

import (
	"fmt"
	"time"
)

func workPool(id int,jobs <-chan int, results chan<- int){
	for job := range jobs {
		fmt.Println("worker",id,"start job",job)
		time.Sleep(time.Second)
		fmt.Println("worker",id,"done job",job)
		results<-job*2
	}
}
func main() {
	jobs := make(chan int ,100)
	results := make(chan int ,100)
	for work:=1;work <=3; work++{
		go workPool(work,jobs,results)
	}
	for job:=1;job<=5;job++{
		jobs <- job
	}
	//close(jobs)
	for a:=1;a<=5;a++{
		fmt.Println(<-results)
	}
}