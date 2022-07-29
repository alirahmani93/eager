package main

import (
	"fmt"
	"io"
	"net/http"
)

func main(){
	fmt.Println("hello web server on go!")
	http.HandleFunc("/about",about)
	http.HandleFunc("/contact",contact)

	fmt.Println("server is running on port :8080 ... :)")

	http.ListenAndServe(":8080",nil)
}


func about(w http.ResponseWriter, r *http.Request){
	io.WriteString(w,"<p style='color:red'> about</p>")
	fmt.Println("about ...")
}
func contact(w http.ResponseWriter, r *http.Request){
	fmt.Println("contact ...")
}