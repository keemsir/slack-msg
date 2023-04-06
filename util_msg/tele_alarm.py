import telegram

def tele_msg(TOKEN: str, ID: int, MSG: str='Task is completed. :thumbsup:'):
  
  # TOKEN: Input the token
  # ID: Input the chat ID
  # MSG: Input the message
  
  bot = telegram.Bot(token=TOKEN)
  bot.sendMessage(chat_id=ID, text=MSG)


def tele_img(TOKEN: str, ID: int, IMG_PATH: str):
  
  # TOKEN: Input the token
  # ID: Input the chat ID
  # MSG: Input the message
  
  bot = telegram.Bot(token=TOKEN)
  bot.send_photo(chat_id=ID, photo=open(IMG_PATH, 'rb'))
  
