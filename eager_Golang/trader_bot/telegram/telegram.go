package telegram

import (
	"fmt"
	"log"
	"net/http"
	"net/url"
)

func SendMessage(chatId string, text string) {
	token := "5590095722:AAHotV4ESCKSgh12iKoW51CMwiUZZyorAsM"
	URL := "https://api.telegram.org/bot" + token + "/sendMessage"
	telegramUrl, err := url.Parse(URL)
	if err != nil {
		log.Println(err)
	}

	values := telegramUrl.Query()
	values.Add("chat_id", chatId)
	values.Add("text", text)
	values.Add("parse_mode", "html")
	telegramUrl.RawQuery = values.Encode()
	fmt.Println(telegramUrl)

	response, err := http.Get(telegramUrl.String())

	fmt.Println(response.StatusCode)
	if response.StatusCode != 200 {
		fmt.Println(response)
	}
	if err != nil {
		fmt.Println(err)
	}
	defer response.Body.Close()
	fmt.Println("message sent.")
}
