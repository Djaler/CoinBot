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
        self._updater.dispatcher.add_handler(
            CommandHandler('bitcoin', self._get_bitcoin_price))
        self._updater.dispatcher.add_handler(
            CommandHandler('bitcoin_cash', self._get_bitcoin_cash_price))
        self._updater.dispatcher.add_handler(
            CommandHandler('bitcoin_gold', self._get_bitcoin_gold_price))
    
    @staticmethod
    def _get_bitcoin_price(bot, update):
        message = update.message

        text = "Current Bitcoin price - ${}".format(Bot._get_price("bitcoin"))
        bot.send_message(chat_id=message.chat_id, text=text)

    @staticmethod
    def _get_bitcoin_cash_price(bot, update):
        message = update.message
    
        text = "Current Bitcoin Cash price - ${}".format(
            Bot._get_price("bitcoin-cash"))
        bot.send_message(chat_id=message.chat_id, text=text)

    @staticmethod
    def _get_bitcoin_gold_price(bot, update):
        message = update.message
    
        text = "Current Bitcoin Gold price - ${}".format(
            Bot._get_price("bitcoin-gold"))
        bot.send_message(chat_id=message.chat_id, text=text)

    @staticmethod
    def _get_price(name):
        url = "https://api.coinmarketcap.com/v1/ticker/{}"
    
        response = requests.get(url.format(name))
        return response.json()[0]['price_usd']
