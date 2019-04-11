package main

import (
	"flag"
	"fmt"
)

func main() {
	wordFlags := flag.String("word","hello","word description")
	linesFlags := flag.Int("line",1,"line description")
	var svar string
	flag.StringVar(&svar,"svar","aa","svar description")
	flag.Parse()
	fmt.Println("word",*wordFlags)
	fmt.Println("lines",*linesFlags)
	fmt.Println("svar",svar)
	fmt.Println("tail",flag.Args())
}


//CLFlags -word=opt a1 a2 a3 -numb=7
//word: opt
//lines: 1
//svar: svar
//tail: [a1 a2 a3 -numb=7]