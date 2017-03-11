import os

import requests
from telegram.ext import CommandHandler, Updater


class Bot:
    def __init__(self, token, debug=False):
        self._token = token
        self._updater = Updater(token)
        self._debug = debug
        
        self._init_handlers()
    
    def run(self):
        port = int(os.environ.get('PORT', '5000'))
        self._updater.start_webhook(listen='0.0.0.0', port=port,
                                    url_path=self._token)
        self._updater.bot.set_webhook(os.environ.get("URL") +
                                      self._token)
        self._updater.idle()
    
    def _init_handlers(self):
        self._updater.dispatcher.add_handler(CommandHandler('rate', self._check_rate))
    
    @staticmethod
    def _check_rate(bot, update):
        message = update.message
        
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        
        response = requests.get(url)
        rate = response.json()['bpi']['USD']['rate_float']
        
        text = "Current Bitcoin rate - ${}".format(rate)
        bot.send_message(chat_id=message.chat_id, text=text)
