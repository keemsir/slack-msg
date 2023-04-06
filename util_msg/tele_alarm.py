import telegram

def tele_msg(TOKEN: str, ID: int, MSG: str='Task is completed. :thumbsup:'):
  
  # TOKEN: Input the token
  # ID: Input the chat ID
  # MSG: Input the message
  
  bot = telegram.Bot(token=TOKEN)
  bot.sendMessage(chat_id=ID, text=MSG)
