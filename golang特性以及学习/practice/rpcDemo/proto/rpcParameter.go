package proto
//定义rpc调用的参数
type ArithmeticMultiplyArgs struct {
	A, B int
}
type ArithmeticMultiplyReply int

type ArithmeticDivideArgs struct {
	A, B int
}
type ArithmeticDivideReply struct {
	Quo, Rem int
}