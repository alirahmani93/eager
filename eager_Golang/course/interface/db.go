package interface 
 import (
	"fmt"
)

type productInterface interface{
	list()
	insert()
	update()
	counter(i int)int
}

type handler struct{ // like class in pthon
	DB string // string must convet to database connection
	num int
}

func (h handler)list(){
	// h.num methods have sturcts values
	fmt.Println("this is list")
}

func (h handler)insert(){
	fmt.Println("insert to model")
}

func (h handler)update(){
	fmt.Println("Update database")
}

func (h handler)counter(i int)int{
	i++ 
	return i
}