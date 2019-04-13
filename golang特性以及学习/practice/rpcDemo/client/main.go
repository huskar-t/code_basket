package main

import (
	"fmt"
	"log"
	"net/rpc/jsonrpc"
	. "rpcDemo/proto"
)

func main() {
	//if len(os.Args) != 2 {
	//	fmt.Println("Usage: ", os.Args[0], "server:port")
	//	log.Fatal(1)
	//}
	//service := os.Args[1]
	service := "127.0.0.1:1234"

	client, err := jsonrpc.Dial("tcp", service)
	if err != nil {
		log.Fatal("dialing:", err)
	}
	// Synchronous call
	argsMultiply := ArithmeticMultiplyArgs{A: 17, B: 8}
	var reply ArithmeticMultiplyReply
	err = client.Call("Arithmetic.Multiply", argsMultiply, &reply)
	if err != nil {
		log.Fatal("Arithmetic error:", err)
	}
	fmt.Printf("Arith: %d*%d=%d\n", argsMultiply.A, argsMultiply.B, reply)

	argsDivide := ArithmeticDivideArgs{A: 12, B: 0}
	var quot ArithmeticDivideReply
	err = client.Call("Arithmetic.Divide", argsDivide, &quot)
	if err != nil {
		log.Fatal("Arithmetic error:", err)
	}
	fmt.Printf("Arith: %d/%d=%d remainder %d\n", argsDivide.A, argsDivide.B, quot.Quo, quot.Rem)

}