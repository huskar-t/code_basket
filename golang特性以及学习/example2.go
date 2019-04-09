package main

import (
	"fmt"
	"os"
)

//for range()

func demoForRange() {
	//for {
	//	//dosth
	//}
	//多重赋值，实现反序
	a := []int{1, 2, 3, 4, 5}
	for i, j := 1, len(a)-1; i < j; i, j = i+1, j-1 {
		a[i], a[j] = a[j], a[i]
	}
	fmt.Println(a)
	alist := []int{1, 2, 3, 4, 5}
	//遍历列表
	for index, value := range (alist) {
		fmt.Println(index, value)
	}
	//遍历字典
	amap := make(map[string]string)
	amap["123"] = "asd"
	for key, value := range (amap) {
		fmt.Print(key, value)
	}
}

func demoDefer() {
	f, err := os.Open("token")
	if err != nil {
		fmt.Println("")
		return
	}
	defer func() {
		_ = f.Close()
	}()
}

//类型+方法=对象
type Myint int

func (m Myint) Less(b Myint) bool {
	return m < b
}
func demoStruct() {
	var a Myint = 1

	if a.Less(2) {
		//dosth
	}
}

type Person struct {
	Name string
	Age  int
}

func (p Person) GetName() string {
	return p.Name
}
func (p *Person) SetName(name string) {
	p.Name = name
}

//对象继承(struct 匿名组合)
type Base struct {
	Name string
}

func (b Base) GetName() string {
	return b.Name
}

type Foo struct {
	Base //匿名实现集成，Base中的方法 Foo可以直接调用
}

func demoFoo() {
	var foo Foo
	foo.GetName()
}

//只有大写开头的成员才能导出包外被使用

//接口
//使用interface定义，接口不需要被继承，任何对象只要实现了借口中的方法就实现了此接口
type IFile interface {
	Read(buf []byte) (n int, err error)
	Write(buf [] byte) (n int, err error)
	Seek(off int64, whence int) (pos int64, err error)
	Close() error
}
type IReader interface {
	Read(buf []byte) (n int, err error)
}
type IWriter interface {
	Write(buf []byte) (n int, err error)
}
type ICloser interface {
	Close() error
}

//定义一个File对象
type File struct {
	fileName string
}

func (f *File) Read(buf []byte) (n int, err error) {
	return 0, nil
}
func (f *File) Write(buf []byte) (n int, err error) {
	return 0, nil
}
func (f *File) Seek(off int64, whence int) (pos int64, err error) {
	return 0, nil
}
func (f *File) Close() error {
	return nil
}
func demoFile() {
	var file1 IFile = new(File)
	var file2 IReader = new(File)
	var file3 IWriter = new(File)
	var file4 ICloser = new(File)
	_, _, _, _ = file1, file2, file3, file4
	// 因为File实现了所有接口的方法，所有File可以赋值给四个接口变量
}

//接口查询，查看对象是否实现接口 (使用类型判断方法)
type demoInterface struct {
	s interface{}
}

func selectInterface() {
	var file1 demoInterface
	if file5, ok := file1.s.(IWriter); ok {
		_, _ = file5.Write(nil)
	}
}

//接口组合，可以像struct一样组合成一个新接口
type ReadWriter interface {
	IReader
	IWriter
}

// 完全等同于下面写法
type ReadWriter2 interface {
	Read(p []byte) (n int, err error)
	Write(p []byte) (n int, err error)
}

//空接口interface{}，可以接受任何类型
func demoEmptyInterface(){
	var v1 interface{} = 1     //  int interface{}
	var v2 interface{} = "abc" //  string interface{}
	var v3 interface{} = &v2   //  *interface{} interface{}
	var v4 interface{} = struct{ X int }{1}
	var v5 interface{} = &struct{ X int }{1}
	_, _, _, _, _ = v1, v2, v3, v4, v5
}

//类型转换，类型查询使用.(traget type)来判断
func demoType(){
	var v1 interface{} = 123
	switch v :=v1.(type) {
	case int:
		fmt.Println("int 型",v)
	case string:
		fmt.Println("string 型")
	}
	tes := make(map[string]interface{})
	tes["a"] = "abc"
	tes["b"] = 123
	value,ok := tes["a"].(string)
	value2,ok2 := tes["a"].(int)
	fmt.Println(value,ok,value2,ok2)
}

//类型强转，只有兼容的对象可以进行转换
func dempChangeType(){
	var var1 int =1
	var2 := float64(var1)
	var3 := int64(var1)
	var4 := new(int32)//var4为指针变量
	var5 := (*int32)(var4)
	_,_,_,_,_ = var1,var2,var3,var4,var5
}