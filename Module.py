# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:50:05 2020

@author: Lukiouss
"""
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.loop import MessageLoop
import telepot
import requests
import csv 
import json
import pytz
import re
import sys
import time

bot = telepot.Bot('#')
bot.getMe()


def Model():
    pass

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    bot.sendMessage(chat_id, 'Skeleton')

bot.message_loop(handle)

while 1:
    time.sleep(10)
