package main

import (
	"fmt"
	"time"
	_ "time"
)

func main() {
	println("hello go land ")
	fmt.Println(false || false)

	for i := 0; i < 5; i++ {
		//print(i)
		if i/2 != 1 {
			fmt.Println(i, "  ", i/2)
		} else if i/2 == 0 {
			fmt.Printf("is is ZERO")
		} else {
			fmt.Print(i, "  ", "blah")
		}
	}
	x := 2
	fmt.Printf("Write", x, "as")
	switch x {
	case 1:
		fmt.Printf("one", x)
	case 5:
		fmt.Printf("two :", x)
	case 3:
		fmt.Printf("three :", x)
	}

	switch time.Now().Weekday() {
	case time.Friday:
		fmt.Printf("yeeeah this is friday")
	case time.Saturday:
		fmt.Printf("yeeeah work time")
	}
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("It's before noon")
	default:
		fmt.Println("It's after noon")
	}
}
