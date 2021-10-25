

# bot = telebot.TeleBot(TOKEN, parse_mode="HTML") # You can set parse_mode by default. HTML or MARKDOWN

# # logger = telebot.logger
# # telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.

# # logging.basicConfig(level=logging.DEBUG,
# #                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



# @bot.message_handler(commands=['start'])
# def send_welcome(m):
#     user_markup = types.ReplyKeyboardMarkup(True, True)
#     user_markup.row(question1,question2 )
#     user_markup.row(question3,question17)
#     user_markup.row(question4,question18)
#     user_markup.row(question5,question38)
#     user_markup.row(question6)
#     user_markup.row(question7)
#     user_markup.row(question8)
#     user_markup.row(question9)
#     user_markup.row(question10)
#     user_markup.row(question11)
#     user_markup.row(question12)
#     user_markup.row(question13)
#     user_markup.row(question14)
#     user_markup.row(question15)
#     user_markup.row(question16)
#     user_markup.row(question19)
#     user_markup.row(question20)
#     user_markup.row(question21)
#     user_markup.row(question22,question23)
#     user_markup.row(question24)
#     user_markup.row(question25)
#     user_markup.row(question26)
#     user_markup.row(question27)
#     user_markup.row(question28)
#     user_markup.row(question29)
#     user_markup.row(question30)
#     user_markup.row(question31)
#     user_markup.row(question32)
#     user_markup.row(question33)
#     user_markup.row(question34)
#     user_markup.row(question35)
#     user_markup.row(question36)
#     user_markup.row(question37)
#     user_markup.row(question39)
#     user_markup.row(question40)
#     cid = m.chat.id
#     line1 = 'Hello, I\'m Adigun 🤖! Press any button below to interact with me. You will love using me to get Blockchain information.'
#     msg = line1
#     bot.send_message(cid, msg, reply_markup=user_markup)


# # main menu
# @bot.message_handler(commands=['menu'])
# @bot.message_handler(regexp="menu")
# def main_menu(m):
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
#     user_markup.row(question1,question2 )
#     user_markup.row(question3,question17)
#     user_markup.row(question4,question18)
#     user_markup.row(question5,question38)
#     user_markup.row(question6)
#     user_markup.row(question7)
#     user_markup.row(question8)
#     user_markup.row(question9)
#     user_markup.row(question10)
#     user_markup.row(question11)
#     user_markup.row(question12)
#     user_markup.row(question13)
#     user_markup.row(question14)
#     user_markup.row(question15)
#     user_markup.row(question16)
#     user_markup.row(question19)
#     user_markup.row(question20)
#     user_markup.row(question21)
#     user_markup.row(question22,question23)
#     user_markup.row(question24)
#     user_markup.row(question25)
#     user_markup.row(question26)
#     user_markup.row(question27)
#     user_markup.row(question28)
#     user_markup.row(question29)
#     user_markup.row(question30)
#     user_markup.row(question31)
#     user_markup.row(question32)
#     user_markup.row(question33)
#     user_markup.row(question34)
#     user_markup.row(question35)
#     user_markup.row(question36)
#     user_markup.row(question37)
#     user_markup.row(question39)
#     user_markup.row(question40)
#     cid = m.chat.id
#     user_msg = 'Welcome to the main menu.\n please, select an option \n'
#     bot.send_message(cid, user_msg, reply_markup=user_markup)


# # help details
# @bot.message_handler(regexp="Help")
# def command_help(m):
#     cid = m.chat.id
#     help_text = "Adigun 🤖: Send my creator *@Josylad* a private message if you need help with anything."
#     bot.send_message(cid, help_text, parse_mode='Markdown')


# @bot.message_handler(regexp='^What is Blockchain$')
# def send_answer(m):
#     user_msg = answer1
#     bot.reply_to(m, user_msg)

# #fixing this regex part was serious work, but it works now!
# @bot.message_handler(regexp='^What is blockchain software$')
# def send_answer(m):
#     user_msg = answer2
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What Is A Private Blockchain$')
# def send_answer(m):
#     user_msg = answer3
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What Is A Smart Contract$')
# def send_answer(m):
#     user_msg = answer4
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is Mining$')
# def send_answer(m):
#     user_msg = answer5
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^How does a blockchain work$')
# def send_answer(m):
#     user_msg = answer6
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is a blockchain application$')
# def send_answer(m):
#     user_msg = answer7
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What are the benefits of blockchain technology$')
# def send_answer(m):
#     user_msg = answer8
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is the blockchain revolution$')
# def send_answer(m):
#     user_msg = answer9
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is decentralized finance$')
# def send_answer(m):
#     user_msg = answer10
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is a block in a blockchain$')
# def send_answer(m):
#     user_msg = answer11
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^What is a blockchain wallet$')
# def send_answer(m):
#     user_msg = answer12
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^How Blockchain Can Be Used In Businesses$')
# def send_answer(m):
#     user_msg = answer13
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What are the Types of Blockchain$')
# def send_answer(m):
#     user_msg = answer14
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^Is Blockchain Hackable or Not Hackable$')
# def send_answer(m):
#     user_msg = answer15
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What is Blockchain Consensus Algorithms$')
# def send_answer(m):
#     user_msg = answer16
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What is Proof of Work$')
# def send_answer(m):
#     user_msg = answer17
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What is Proof of Stake$')
# def send_answer(m):
#     user_msg = answer18
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What are the Key features of Blockchain$')
# def send_answer(m):
#     user_msg = answer19
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^How Does Blockchain Work$')
# def send_answer(m):
#     user_msg = answer20
#     bot.reply_to(m, user_msg)

# @bot.message_handler(regexp='^Is there any restriction that only a particular industry should utilize Blockchain$')
# def send_answer(m):
#     user_msg = answer21
#     bot.reply_to(m, user_msg)

    
# @bot.message_handler(regexp='^What is a cryptocurrency$')
# def send_answer(m):
#     user_msg = answer22
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^Why use cryptocurrency"$')
# def send_answer(m):
#     user_msg = answer23
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^How many cryptocurrencies exist in the web$')
# def send_answer(m):
#     user_msg = answer24
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What was the first cryptocurrency$')
# def send_answer(m):
#     user_msg = answer25
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='^What are the most common cryptocurrencies$')
# def send_answer(m):
#     user_msg = answer26
#     bot.reply_to(m, user_msg)

    
# @bot.message_handler(regexp='^What is alternative currency$')
# def send_answer(m):
#     user_msg = answer27
#     bot.reply_to(m, user_msg)

        
# @bot.message_handler(regexp='^Is it that difficult to obtain cryptocurrency coin$')
# def send_answer(m):
#     user_msg = answer28
#     bot.reply_to(m, user_msg)

        
# @bot.message_handler(regexp='^What is Cryptocurrency Mining$')
# def send_answer(m):
#     user_msg = answer29
#     bot.reply_to(m, user_msg)

        
# @bot.message_handler(regexp='^Why should I get involved in cryptocurrency$')
# def send_answer(m):
#     user_msg = answer30
#     bot.reply_to(m, user_msg)

        
# @bot.message_handler(regexp='^What is a cryptocurrency wallet$')
# def send_answer(m):
#     user_msg = answer31
#     bot.reply_to(m, user_msg)

        
# @bot.message_handler(regexp='^What is cryptocurrency exchange and market$')
# def send_answer(m):
#     user_msg = answer32
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^How is the cryptocurrency value determined$')
# def send_answer(m):
#     user_msg = answer33
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^What are the exciting reason for you to get involved with the digital currency$')
# def send_answer(m):
#     user_msg = answer34
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^What will be the worst part about cryptocurrencies$')
# def send_answer(m):
#     user_msg = answer35
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^Which cryptocurrency is the best to date$')
# def send_answer(m):
#     user_msg = answer36
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^Is there a fake cryptocurrency$')
# def send_answer(m):
#     user_msg = answer37
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^Is Cryptocurrency Legal$')
# def send_answer(m):
#     user_msg = answer38
#     bot.reply_to(m, user_msg)

            
# @bot.message_handler(regexp='^What is the main difference between tokens and cryptocurrencies$')
# def send_answer(m):
#     user_msg = answer39
#     bot.reply_to(m, user_msg)

                
# @bot.message_handler(regexp='^What is the difference between cryptocurrency and digital currency$')
# def send_answer(m):
#     user_msg = answer40
#     bot.reply_to(m, user_msg)


# @bot.message_handler(regexp='')
# def send_answer(m):
#     user_msg = 'Hi, it seems you have entered an invalid comman, kindly use the menu or reply with "menu"'
#     bot.reply_to(m, user_msg)
# # Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# # - none_stop: True/False (default False) - Don't stop polling when receiving an error from the Telegram servers
# # - interval: True/False (default False) - The interval between polling requests
# #           Note: Editing this parameter harms the bot's response time
# # - timeout: integer (default 20) - Timeout in seconds for long polling.

# bot.polling()


#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# #!/usr/bin/env python
import os
import telebot 
import logging
from telebot import types
from replies import *
from decouple import config



TOKEN = config("TOKEN")
# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()