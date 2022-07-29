package main

import(
	"fmt"
	"app/config"
	"app/database"

)

func main(){
	config.SetConfig()
	database.Connection()


	fmt.Println(config.Config.Port)
	fmt.Println("Hoora !! OK !!! :)")
}