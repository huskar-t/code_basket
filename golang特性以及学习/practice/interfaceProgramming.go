package main

import (
	"fmt"
	"math"
)

type geometry interface {
	area()float64
	prem()float64
}
type rect struct {
	width float64
	height float64
}
type circle struct {
	redius float64
}

func (c circle)area()float64{
	return math.Pi*math.Pow(c.redius,2)
}

func (c circle)prem()float64{
	return 2*math.Pi*c.redius
}

func (r rect)area()float64{
	return r.height*r.width
}

func (r rect)prem()float64{
	return 2*(r.height+r.width)
}

func measure(g geometry){
	fmt.Printf("%#v\n", g)
	fmt.Println(g.area())
	fmt.Println(g.prem())
}

func main()  {
	a := circle{
		redius:11.0,
	}
	b := rect{
		width:2,
		height:12,
	}
	measure(a)
	measure(b)
}