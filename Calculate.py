import telebot
from telebot import types

bot = telebot.TeleBot('6881808634:AAEtqD7fOe7IujW6Rt18XjsPAokd66DGq-4')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('admin', callback_data='btn1')
    button2 = types.InlineKeyboardButton('help', callback_data='btn2')
    button3 = types.InlineKeyboardButton('channel', callback_data='btn3')
    button4 = types.InlineKeyboardButton('About', callback_data='btn4')
    markup.add(button1, button2)
    markup.add(button3, button4)
    bot.send_message(message.chat.id, f'Hello 👋 {message.from_user.first_name}\n'
     'Welcome to the bot\n'
 'This bot acts as a calculator for you and the things it calculates\n'
 '- Addition\n'
 '- Subtract\n'
 '- Multiply\n'
 '- Divide\n'
  'If you are unsure how to use it, click on the can help button below\n'
  'powered by @amiir_exe', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'btn1':
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton('Back', callback_data='back')
        markup.add(back_button)
        bot.edit_message_text('Created by @amiir_exe:', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == 'btn2':
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton('Back', callback_data='back')
        markup.add(back_button)
        bot.edit_message_text('You clicked help . Choose another option:\nAvailable commands:\n'
                              '/add [number1] [number2] - Add two numbers\n'
                              '/subtract [number1] [number2] - Subtract two numbers\n'
                              '/multiply [number1] [number2] - Multiply two numbers\n'
                              '/divide [number1] [number2] - Divide two numbers', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

    elif call.data == 'btn3':
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton('Back', callback_data='back')
        markup.add(back_button)
        channel_link = 'tech it -> <a href="https://t.me/+FWz0h6fN0BtjMmFk">You can join the channel here</a>'
        bot.edit_message_text(channel_link, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        
    elif call.data == 'btn4':
        markup = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton('Back', callback_data='back')
        markup.add(back_button)
        channel_link ='⚡️I can calculate for you \n'\
        '▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'\
        '🤖 Bot: calculate bot \n'\
        '💥 Server: none\n'\
        '🧰 Programming Language: Python\n'\
        '🗿 Not a Opensource Project\n'\
        '✅ if owner in online Active ✓\n'\
        '👨‍💻  Developer:  <a href="https://t.m/Amiir_exe">ᴀᴍɪʀㅤeXeㅤ🇸🇩</a>\n'\
        '▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n'\
        '\n'\
        '⚡️ Bot By :- <a href="https://t.me/+FWz0h6fN0BtjMmFk">pythonicAY</a>'
        
        bot.edit_message_text(channel_link, chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup, parse_mode='HTML')
        
    elif call.data == 'back':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton('admin', callback_data='btn1')
        button2 = types.InlineKeyboardButton('help', callback_data='btn2')
        button3 = types.InlineKeyboardButton('channel', callback_data='btn3')
        button4 = types.InlineKeyboardButton('About', callback_data='btn4')
        markup.add(button1, button2)
        markup.add(button3, button4)
        bot.edit_message_text(f'Hello {call.message.chat.first_name}!\n'
                              'Welcome to the bot\n'
                              'This bot acts as a calculator for you and the things it calculates\n'
                              '- Addition\n'
                              '- Subtract\n'
                              '- Multiply\n'
                              '- Divide\n'
                              'If you are unsure how to use it, click on the can help button below\n'
                              'powered by @amiir_exe ', chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)


@bot.message_handler(commands=['add'])
def add_numbers(message):

    args = message.text.split()[1:]

    if len(args) != 2:
        bot.reply_to(message, "Invalid number of arguments. Usage: /add [number1] [number2]")
    else:
        try:
            result = float(args[0]) + float(args[1])
            bot.reply_to(message, f"Result: {result}")
        except ValueError:
            bot.reply_to(message, "Invalid number format. Usage: /add [number1] [number2]")
@bot.message_handler(commands=['subtract'])
def subtract_numbers(message):
    
    args = message.text.split()[1:]
    
    if len(args) != 2:
        bot.reply_to(message, "Invalid number of arguments. Usage: /subtract [number1] [number2]")
    else:
        try:
            
            result = float(args[0]) - float(args[1])
            
            bot.reply_to(message, f"Result: {result}")
        except ValueError:
            bot.reply_to(message, "Invalid number format. Usage: /subtract [number1] [number2]")


@bot.message_handler(commands=['multiply'])
def multiply_numbers(message):
    
    args = message.text.split()[1:]
    
    if len(args) != 2:
        bot.reply_to(message, "Invalid number of arguments. Usage: /multiply [number1] [number2]")
    else:
        try:
            
            result = float(args[0]) * float(args[1])
            
            bot.reply_to(message, f"Result: {result}")
        except ValueError:
            bot.reply_to(message, "Invalid number format. Usage: /multiply [number1] [number2]")

@bot.message_handler(commands=['divide'])
def divide_numbers(message):
    
    args = message.text.split()[1:]
    
    if len(args) != 2:
        bot.reply_to(message, "Invalid number of arguments. Usage: /divide [number1] [number2]")
    else:
        try:
            
            result = float(args[0]) / float(args[1])
            
            bot.reply_to(message, f"Result: {result}")
        except ZeroDivisionError:
            bot.reply_to(message, "Cannot divide by zero.")
        except ValueError:
            bot.reply_to(message, "Invalid number format. Usage: /divide [number1] [number2]")
print("bot is done")
bot.polling()
