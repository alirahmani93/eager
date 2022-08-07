package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"reflect"
	"strconv"
	"strings"
	"time"
	"trader_bot/telegram"
)

type binanceData [][]interface{}
type candle struct {
	Symbol   string
	Interval string

	Open   float64
	Close  float64
	High   float64
	Low    float64
	Volume float64

	UpperShadowPercent  int32
	BottomShadowPercent int32

	OpenTime  int
	CloseTime int
}

func convertToFloat64(s string) float64 {
	f, _ := strconv.ParseFloat(s, 64)
	return f
}
func convertToInt(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func main() {
	fmt.Println("hello trader.. get make some money :) ")

	for {
		msg := getData("BTCUSDT", "1d")
		fmt.Println(reflect.TypeOf(msg))
		fmt.Println(msg)
		//fmt.Println(msg[0])
		telegram.SendMessage("105536324", "hi ali ...")
		time.Sleep(time.Second * 1)
	}

}
func getData(symbol string, interval string) string {
	var binanceUrl = "https://www.binance.com/api/v3/uiKlines?limit=1&symbol=" + symbol + "&interval=" + interval

	response, err := http.Get(binanceUrl)

	if err != nil {
		log.Println(err)
	}
	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)

	data := binanceData{}
	d := json.NewDecoder(strings.NewReader(string(body)))
	d.UseNumber()
	if err := d.Decode(&data); err != nil {
		log.Fatal("err:", err)
	}
	err = json.Unmarshal(body, &data)
	if err != nil {
		log.Println(err)
	}

	var candles []candle
	var candle candle
	for _, v := range data {
		candle.OpenTime = convertToInt(fmt.Sprint(v[0]))
		candle.OpenTime = convertToInt(fmt.Sprint(v[0]))
		candle.CloseTime = convertToInt(fmt.Sprint(v[6]))
		candle.Open = convertToFloat64(fmt.Sprint(v[1]))
		candle.Close = convertToFloat64(fmt.Sprint(v[4]))
		candle.High = convertToFloat64(fmt.Sprint(v[2]))
		candle.Low = convertToFloat64(fmt.Sprint(v[3]))
		candle.Volume = convertToFloat64(fmt.Sprint(v[5]))
		fmt.Println("price is", candle.Close)
		candles = append(candles, candle)
	}
	return candle.Symbol
}
