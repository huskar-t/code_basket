package functions

import (
	"errors"
	."rpcDemo/proto"
	)
type Arithmetic int
func (t *Arithmetic) Multiply(args *ArithmeticMultiplyArgs, reply *ArithmeticMultiplyReply) error {
	*reply = ArithmeticMultiplyReply(args.A * args.B)
	return nil
}

func (t *Arithmetic) Divide(args *ArithmeticDivideArgs, quo *ArithmeticDivideReply) error {
	if args.B == 0 {
		return errors.New("divide by zero")
	}
	quo.Quo = args.A / args.B
	quo.Rem = args.A % args.B
	return nil
}