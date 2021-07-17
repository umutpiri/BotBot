import discord
import os
from blockchain import Blockchain
from gif import Gif
from quote import Quote
from calculator import Calculator
from gamble import Gamble
from corona import Corona
from exchange import Exchange
from investing import Investing
from timer import Timer
from keep_alive import keep_alive
from help_me import help1,help2
from taboo import Taboo

client = discord.Client()
gif = Gif(os.getenv('GIPHY_API_KEY'))
blockchain = Blockchain(os.getenv('BTC_API_KEY'))
corona = Corona(os.getenv('RAPID_API_KEY'))
exchange = Exchange(os.getenv('RAPID_API_KEY'))
investing = Investing()
quote = Quote()
calculator = Calculator()
gamble = Gamble()
taboo = Taboo()

category_words={
  "hi": ['hi', 'hello', 'hey'],
  "pm": ['pm', 'private', 'dm'],
  "timer": ['timer', 'time', 't'],
  "inspire": ['inspire', 'ins'],
  "bitcoin": ['bitcoin', 'xrp', 'eth', 'btc', 'b'],
  "gif": ['gif', 'g'],
  "coin": ['coin', 'toss', 'flip', 'heads', 'tails', 'c'],
  "random": ['random', 'rand', 'r'],
  "corona": ['corona', 'covid', 'korona'],
  "exchange": ['exchange', 'convert', 'e', 'dollar', 'dolar', 'usd'],
  "investing": ['investing', 'inv', 'i'],
  "help": ['help', 'h'],
  "taboo": ['taboo', 'tabu']
}


def is_starts_with(msg, category):
  command = msg.split()[0]
  return command in category_words[category]


@client.event
async def on_ready():
  print('Ready Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!'):
    msg = msg[1:]
    if is_starts_with(msg, "hi"):
      await message.channel.send('Hello!')
    elif is_starts_with(msg, "help"):
      await message.channel.send(help1)
      await message.channel.send(help2)
    elif is_starts_with(msg, 'pm'):
      await message.author.send("HELLO ;)")
    elif is_starts_with(msg, 'timer'):
      timer = Timer(msg, message.channel)
      await timer.start_timer()
    elif is_starts_with(msg, 'inspire'):
      await message.channel.send(quote.get_random())
    elif is_starts_with(msg, 'bitcoin'):
      await message.channel.send(investing.get_btc_usd(msg))
    elif is_starts_with(msg, 'gif'):
      await message.channel.send(gif.get_random(msg))
    elif is_starts_with(msg, 'coin'):
      await message.channel.send(gamble.coin_flip())
    elif is_starts_with(msg, 'random'):
      await message.channel.send(gamble.get_random_number(msg)) 
    elif is_starts_with(msg, 'corona'):
      await message.channel.send(corona.get_country_data(msg))
    elif is_starts_with(msg, 'exchange'):
      await message.channel.send(exchange.get_currency_exchange_rate(msg))
    elif is_starts_with(msg, 'investing'):
      await message.channel.send(investing.get_btc_usd(msg))
    elif is_starts_with(msg, 'taboo'):
      await message.author.send(taboo.get_random(msg))
    elif msg.startswith('fifa'):
      await message.channel.send('FIFA KONUŞMAYIN MQ YETER')
    elif msg.startswith('mc'):
      await message.channel.send('FIFA KONUŞMAYIN MQ YETER')
    elif msg.startswith('malbahran'):
      await message.channel.send('MAL BAHRAN', tts=True)
    elif msg.startswith('helalbahran'):
      await message.channel.send('HELAL BAHRAN', tts=True)
    elif msg.startswith('atmeren'):
      await message.channel.send('ATM EREN', tts=True)
    elif calculator.is_equation(msg):
      await message.channel.send(calculator.calculate())
    

keep_alive()
client.run(os.getenv('DISCORD_TOKEN'))