import logging 
from aiogram import Bot, Dispatcher, executor, types #package
from dotenv import load_dotenv 
import os 

# accessing token from .env 
load_dotenv()
api_token = os.getenv("TOKEN")
print(api_token)

# configure logging 
logging.basicConfig(level=logging.INFO)

## initializing bot and dispatcher  
bot = Bot(token = api_token)
dp = Dispatcher() # helps u to make the connection with ur telegram bot. 
    
@dp.message_handler()
async def echo(message: types.Message) -> None:
   '''
   This will return echo
   '''
   await message.answer(message.text)


if __name__ == "__main__":
   executor.start_polling(dp, skip_updates= True)