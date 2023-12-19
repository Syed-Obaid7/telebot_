from dotenv import load_dotenv
import os 
from aiogram import Bot, Dispatcher, executor, types
import openai 
import sys


class Reference : 
    '''
    A class to store previously response from the ChatGPT API. 
    '''

    def __init__(self) -> None : # returns none 
        self.response = ""

## accessing OPENAI Key 
load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY") # authenticate with OpenAI

reference = Reference()

TOKEN = os.getenv("TOKEN") # bot token 

## > model name  
MODEL_NAME = "gpt-3.5-turbo" # gives less charge, so using this :) 
dispatcher = Dispatcher(bot)

## to forget the prev context if required  
def clear_past():
    '''
    A function to clear the prev conversation and context 
    '''
    reference.response = ""

@dispatcher.message_handler(commands=["start"])
async def welcome(message: types.Message) -> None:
   '''
   This handler receives messages with '/start' or '/help' command
   '''
   await message.answer("Hi\nI am AI.MOR bot!\nPowered by AIMOR. How can I assist you?")

## calling clear function
@dispatcher.message_handler(commands=["clear"])
async def clear(message: types.Message):
    '''
    A handler to clear the previous conversation and context.
    '''
    clear_past()
    await message.reply("I've cleared the past conversation and context.")

## helper function -- /help 
@dispatcher.message_handler(command=["help"])
async def helper(message: types.Message):
   """
   A handler to display the help menu
   """
   help_command = """
   Hie! I'm ChatGPT Telegram bot created by AIMOR! Please follow these commands 
   /start - to start the conversation 
   /clear - to clear the past conversation and context 
   /help - to get this help menu.
   Hope, this is useful!! :] 
"""

## The cheese is here. 
@dispatcher.message_handler()
async def chatgpt(message: types.Message): 
    """
    A handler to process the user's i/p and generate a response using the chatGPT API.
    """
    print(f">>> USER : \n\t{message.text}") #prints in the terminal 
    response = openai.ChatCompletion.create(
        model = MODEL_NAME, 
        messages = [
            {"role" : "assistant", "content" : reference.response}, # role assistant 
            {"role" : "user","content" : message.text} # our query 
        ]
    )
    reference.response = response["choices"][0]["message"]["content"]
    print(f">>> chatGPT: \n\t{reference.repsonse}")
    await bot.send_message(chat_id = message.chat.id, text= reference.response)



if __name__ == "__main__" :
    executor.start_polling(dispatcher, skip_updates= True)