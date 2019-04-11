package main

import "fmt"

func main() {
	messages := make(chan string)
	signs := make(chan string)
	select {
	case msg:= <- messages:
		fmt.Println("received message",msg)
	default:
		fmt.Println("no message received")
	}
	msg := "hi"
	select {
	case messages <- msg:
		fmt.Println("sent message", msg)
	default:
		fmt.Println("no message sent")
	}
	select {
	case msg:=<-messages:
		fmt.Println("received message",msg)
	case sig := <- signs:
		fmt.Println("received sign",sig)
	default:
		fmt.Println("no activity")
	}
}

