package config
import(
	"github.com/joho/godotenv"
	"os"
	"log"
)
type config struct{
	Port 		string `json:"port"`
	DB_HOST 	string `json:"db_host"`
	DB_USER 	string `json:"db_user"`
	DB_PASSWORD string `json:"db_password"`
	DB_SSL_MOD 	string `json:"db_ssl_mod"`
	DB_TIMEZONE 	string `json:"db_timezone"`
	DB_PORT 	string `json:"db_port"`
	DB_NAME 	string `json:"db_name"`
}

var Config config
func SetConfig()  {
	err :=godotenv.Load(".env")
	if err != nil{
		log.Fatalf("some error %s",err)
	}

	Config.Port=os.Getenv("Port")
	Config.DB_HOST=os.Getenv("DB_HOST")
	Config.DB_USER=os.Getenv("DB_USER")
	Config.DB_PASSWORD=os.Getenv("DB_PASSWORD")
	Config.DB_SSL_MOD=os.Getenv("DB_SSL_MOD")
	Config.DB_TIMEZONE=os.Getenv("DB_TIMEZONE")
	Config.DB_PORT=os.Getenv("DB_PORT")
	Config.DB_NAME=os.Getenv("DB_NAME")
}