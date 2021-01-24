import discord
import os
from blockchain import Blockchain
from gif import Gif
from quote import Quote
from calculator import Calculator
from gamble import Gamble
from corona import Corona
from exchange import Exchange

client = discord.Client()
gif = Gif(os.getenv('GIPHY_API_KEY'))
blockchain = Blockchain(os.getenv('BTC_API_KEY'))
corona = Corona(os.getenv('RAPID_API_KEY'))
exchange = Exchange(os.getenv('RAPID_API_KEY'))
quote = Quote()
calculator = Calculator()
gamble = Gamble()

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
    if "hello" in msg or "hi" in msg:
      await message.channel.send('Hello!')
    elif "inspire" in msg:
      await message.channel.send(quote.get_random())
    elif "bitcoin" in msg or "blockchain" in msg or "btc" in msg:
      await message.channel.send(blockchain.get_exchange())
    elif "gif" in msg:
      await message.channel.send(gif.get_random())
    elif "coin" in msg or "flip" in msg:
      await message.channel.send(gamble.coin_flip())
    elif "random" in msg:
      await message.channel.send(gamble.get_random_number(msg)) 
    elif "corona" in msg or "korona" in msg:
      await message.channel.send(corona.get_country_data(msg))
    elif "convert" in msg or "conv" in msg or "ex" in msg or "dolar" in msg:
      await message.channel.send(exchange.get_currency_exchange_rate(msg))
    elif calculator.is_equation(msg):
      await message.channel.send(calculator.calculate(msg))
    


client.run(os.getenv('DISCORD_TOKEN'))