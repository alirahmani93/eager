package main
import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main(){ // main function in a go routin

	fmt.Println("start")
	wg.Add(1)
	go task1()

	wg.Add(1)
	go task2()

	wg.Add(1)
	go task3()
	
	fmt.Println("end")

	wg.Wait()
	fmt.Println("end2")	

}

func task1(){
	for i:=0;i<=10;i++{
		fmt.Println(i)
	}
	wg.Done()

}

func task2(){
	for i:=10;i<=20;i++{
		fmt.Println(i)
	}
	wg.Done()

}

func task3(){
	for i:=20;i<=30;i++{
		fmt.Println(i)
	}
	wg.Done()
}

