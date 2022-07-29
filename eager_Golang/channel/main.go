package main
import (
	"fmt"
	"time"
)
func main(){
	fmt.Println("start")
	ch := make(chan int) // unbuffer channel type int
	go bufferChannelPrint(ch)
	msg := <- ch // wait for return sth from ch
	fmt.Println(msg)
	
	fmt.Println("end")


	uch := make(chan int,10) // buffer channel doesn't wate for reciver
	go unBufferChannelPrint(uch)
	// fmt.Println(<- ch)
	// fmt.Println(<- ch) deadlock! error :))
	
	for i:=0; i<cap(uch);i++{
		fmt.Println(<- uch)
	}

	fmt.Println("end")
}

func bufferChannelPrint(ch chan int){
	time.Sleep(time.Second*5)
	ch <- 30
}
func unBufferChannelPrint(uch chan int){
	fmt.Println("cap is: ", cap(uch))
	for i:=0; i<cap(uch);i++{
		// fmt.Println(i)
		uch <- i
	}
	// time.Sleep(time.Second*2)
}