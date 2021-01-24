import requests
import json
from prettytable import PrettyTable


class Blockchain:
  def __init__(self, token):
    self.base_url = "https://api.nomics.com/v1/currencies/ticker?key="+token

  def get_exchange(self):
    res = requests.get(self.base_url+'&ids=BTC,ETH,XRP&interval=1h,1d')
    json_data = json.loads(res.text)

    t = PrettyTable(['Name', 'Price (USD)', 'Change (1H)', 'Change (1D)'])

    exchange_data = []

    for data in json_data:
      exchange_data.append([data['id'], data['price'].rjust(14, '0'), '%' + data['1h']['price_change_pct'], '%' + data['1d']['price_change_pct']])
    
    t.add_rows(exchange_data)

    return "```\n"+str(t)+"\n```"
