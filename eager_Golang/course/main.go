package main

import (
	// "app/MathPackage"
	// "app/printPackage"
	// "app/models"
	// "app/pointer"
	// "app/interface"
	"app/routin"

	"fmt"
	"sync"
	// "reflect"
)

// .... variables .... //
	// var i int = 5

	// var (
	// 	q int =1
	// 	w string="W"
	// 	e bool=true
	// )

	// const (
	// 	PI =3.14
	// 	R =1
	// )
// .... routin .... //
var wg sync.WaitGroup

func main(){
// ..... Variables ..... //
	// fmt.Println(reflect.TypeOf(R))
	// v :=5 // scope in function
	// fmt.Println(v)

	// i=3
	// fmt.Println(i)
	// fmt.Println(q,w,e)
	// fmt.Println(PI*R*R)
	// var x int = 2
	// var y string = "ali rahmani"
	// var b bool
	// fmt.Println(x,y)
	// fmt.Println(y)
	// fmt.Println(b)
	// fmt.Println("hello world")

// ..... package ..... ///
	// result := printPackage.PrintInt(q)
	// result2,result3 := printPackage.PrintIntString(q,w,e)
	// fmt.Println(result)
	// fmt.Println(result2,result3)
	// MathPackage.Sum(i,q)


// .... Array .... //
	// array
	// a1 := [5]int{10,20,30,40,50}
	// a2 := [10]int{10,20,30,40,50}
	// a2[1]=1000
	// fmt.Println(a1)
	// fmt.Println(a2)
	// fmt.Println(len(a2))
	// fmt.Println(cap(a2))

	// a3 :=[12]string{}
	// a3[len(a3)-3]="ali rahmani"
	// fmt.Println(a3)

	// // slices
	// s:=[]int{10,20,30,40,50}
	// s2 := []int{60,70,80}
	// s3:= append(s,s2...)
	// fmt.Println(s3)
	// index := 2 
	// s3 = append(s3[:index],s3[index+1:]...) //
	// fmt.Println(s3)
// .... map .... ///
	// m := map[string]string{
	// 	"k1" : "v1",
	// 	"k2" : "v2",
	// 	"k3" : "v3",
	// }
	// n :=map[string]int{
	// 	"a1":1,
	// 	"a2":2,
	// }
	// m["k4"]="v4"
	// delete(m,"k1")
	// fmt.Println(m)
	// fmt.Println(n)
	// fmt.Println(len(n))

// .... For loop ... //
	// i :=0
	// for {
	// 	i++
	// 	fmt.Println(i)
	// }

	// for (c:=0,c<10;c++){
	// 	fmt.Println(c)
	// }

	// i := 0
	// for i<10{ // like while loop
	// 	i++
	// 	fmt.Println(i)
	// }


	// For range

	// for index,value := range m{
	// 	fmt.Println("index: " + index, "values: "+value)
	// }

// .... Conditions .... //
	// x:=30
	// if x == 4 || x ==3{
	// 	fmt.Println("x = 4 or 3")
	// }else if x >=5 && x<=10{
	// 	fmt.Println("OK")
	// }else{
	// 	fmt.Println("wring")
	// }

	// switch x{
	// case 0:
	// 	fmt.Println("x = 0")
	// case 1:
	// 	fmt.Println("x = 1")
	// case 30:
	// 	fmt.Println("x =30")
	// default:
	// fmt.Println("NO")
	// }
// .... Struct ..... //
	// myUser :=models.User{
	// 	FirstName:"ali",
	// 	LastName:"rahmani",
	// 	CityId:1,
	// 	IsActive:false,
	// }
	// var myUser2 models.User
	// myUser2.FirstName = "maryam"
	// myUser2.LastName="Ghaemi"
	// myUser2.CityId=3
	// myUser2.IsActive=true
	// fmt.Println(myUser)
	// fmt.Println(myUser2)

	// var userArr []models.User

	// userArr=append(userArr,myUser)
	// userArr=append(userArr,myUser2)
	// fmt.Println(userArr)
	// fmt.Println(len(userArr))

	// for _,user := range userArr{
	// 	fmt.Println(user)
	// 	fmt.Println(user.FirstName)

	// }
// .... Pointer .... //
	// var i int = 10 
	// fmt.Println("initial i:",i)
	// // pointer.Increment(i)
	// // fmt.Println("out of func increment i: ", i)
	// pointer.IncrementPointer(i)
	// fmt.Println("out of func increment pointer: ",i)

// .... methods and interface .... //

	// var pi productInterface
	// pi = new(handler) // best practice of create a object 
	// // pi = &handler{} // create object by pointer
	// // pi = handler{} // create object

	// pi.insert()

	// num :=10
	// fmt.Println(pi.counter(num))

	
}

// .... methods and interface .... //
 
	// type productInterface interface{
	// 	list()
	// 	insert()
	// 	update()
	// 	counter(i int)int
	// }

	// type handler struct{ // like class in pthon
	// 	DB string // string must convet to database connection
	// 	num int
	// }

	// func (h handler)list(){
	// 	// h.num methods have sturcts values
	// 	fmt.Println("this is list")
	// }

	// func (h handler)insert(){
	// 	fmt.Println("insert to model")
	// }

	// func (h handler)update(){
	// 	fmt.Println("Update database")
	// }

	// func (h handler)counter(i int)int{
	// 	i++ 
	// 	return i
	// }

