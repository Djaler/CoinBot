import os

# webhook
URL = os.environ.get('URL')
PORT = int(os.environ.get('PORT', '5000'))

# telegram
TOKEN = os.environ.get('TOKEN')
