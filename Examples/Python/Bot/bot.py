from random import *
import telebot
import json
import requests

film = []

API_TOKEN = '6096485263:AAHTp0ib0iEJBnBWsvkEmZ19_bV2AMwBgAM'
bot  = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start_message(message):

    film.append('1')
    film.append('2')
    film.append('3')
    film.append('4')
    bot.send_message(message.chat.id,'film')

@bot.message_handler(commands = ['all'])
def show_all(message):
    try:
        bot.send_message(message.chat.id,"spisok")
        bot.send_message(message.chat.id,',\n'.join(film))
    except:
        bot.send_message(message.chat.id,"spisok")

@bot.message_handler(commands=['save'])
def Save_all(message):
    with open("films.json",'w',encoding='utf-8') as fh:
        fh.write(json.dumps(film,ensure_ascii=False)) 
    bot.send_message(message.chat.id,"Great")

bot.polling()