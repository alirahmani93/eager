package database
import (
	"log"
	
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	

	"app/config"

)
type DB struct{
Conn *gorm.DB
}

func Connection()DB{
	dsn := 	" host=" 		+ config.Config.DB_HOST +
			" user="		+ config.Config.DB_USER +
			" password="	+ config.Config.DB_PASSWORD +
			" port="		+ config.Config.DB_PORT +
			" dbname="		+ config.Config.DB_NAME +
			// " sslmode=" 	+ config.Config.DB_SSL_MOD +
			" timezone="	+ config.Config.DB_TIMEZONE
	
	db,err := gorm.Open(postgres.Open(dsn),&gorm.Config{})
	if err!=nil{
		log.Fatal(err)
	}
	return DB{
		Conn:db,
	}
}