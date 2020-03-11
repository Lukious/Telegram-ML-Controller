
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
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import Imputer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error

bot = telepot.Bot('#')
bot.getMe()

#def Model()
def Model(give_hyperparameter):
    # Generate Figure
    # Make validate score.. Anything is Okay!
    return train_mae_score

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if content_type == 'text':
        text = msg['text']
        mode = text [:5]
        inputed_data = text[6:]
        print(msg['text'])

    if '/runs' in mode:
        bot.sendMessage(chat_id, 'hyperparameter is ' + str(inputed_data))
        bot.sendMessage(chat_id, 'Running...')
        bot.sendMessage(chat_id, Model(float(inputed_data)))    
        bot.sendPhoto(chat_id, open('fig1.jpg','rb'))
        bot.sendPhoto(chat_id, open('svm_conf.jpg','rb'))
    else:
        bot.sendMessage(chat_id, 'Not verified')
        bot.sendPhoto(chat_id, open('fig1.jpg','rb'))

bot.message_loop(handle)

while 1:
    time.sleep(10)
