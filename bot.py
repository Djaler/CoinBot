import os

import requests
from telegram.ext import RegexHandler, Updater

from config import URL, PORT
from utils import format_thousands


class Bot:
    def __init__(self, token, debug=False):
        self._token = token
        self._updater = Updater(token)
        self._debug = debug

        self._session = requests.Session()

        self._init_handlers()
    
    def run(self):
        self._updater.start_webhook(listen='0.0.0.0', port=PORT,
                                    url_path=self._token)
        self._updater.bot.set_webhook(URL + self._token)
        self._updater.idle()
    
    def _init_handlers(self):
        self._updater.dispatcher.add_handler(
            RegexHandler("^/([a-z_]+)$", self._get_currency_price,
                         pass_groups=True))

    def _get_currency_price(self, bot, update, groups):
        currency = groups[0]
    
        info = self._get_info(currency.replace("_", "-"))
    
        text = "Current {} price - ${}".format(info["name"], format_thousands(info["price_usd"], sep=" "))
    
        bot.send_message(chat_id=update.message.chat_id, text=text)
    
    def _get_info(self, name):
        url = "https://api.coinmarketcap.com/v1/ticker/{}"

        response = self._session.get(url.format(name))
        return response.json()[0]
