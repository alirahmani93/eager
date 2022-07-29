package pointer

import "fmt"

func Increment(a int){
	fmt.Println("before increment: ",a)
	a++
	a++
	a++
	a++
	fmt.Println("after increment: ",a)
}
func IncrementPointer(a int){
	var pa *int
	fmt.Println("nil pointer a: ",pa)
	pa = &a // & return stored value in memmory pointer of var a 
	fmt.Println("pointer a: ",pa)

	fmt.Println("nil pointer a: ",pa)
	fmt.Println("before increment by pointer: ",a)
	a++
	a++
	a++
	a++
	fmt.Println("after increment by pointer: ",a)
}