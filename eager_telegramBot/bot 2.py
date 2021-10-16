import telegram #imorted methodts
from telegram.ext import Updater, CommandHandler
import requests
from telegram import ReplyKeyboardMarkup, KeyboardButton 
from telegram.ext.messagehandler import MessageHandler
import json

def start(bot, update):
 button1 = KeyboardButton("hello")
 button2 = KeyboardButton("by")
 keyboard = [button1, button2] 
 reply_markup = telegram.ReplyKeyboardMarkup(keyboard)
 chat_id = update.message.chat_id
 bot.send_message(chat_id=chat_id, text='please choose USD or EUR', reply_markup = reply_markup) # it works and returns text if reply_markup parameter disabled.

def main(): 
 updater = Updater('1340038194:AAF03lVxvrHeT-ALT5Ut-WYErRwuZ0wd7C0')
 dp = updater.dispatcher
 dp.add_handler(CommandHandler('start', start))
 updater.start_polling()
 updater.idle()

main()
