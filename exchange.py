import requests
import json

class Exchange:
  def __init__(self, token):
    self.base_url = "https://alpha-vantage.p.rapidapi.com/query"
    self.headers = {'x-rapidapi-key': 
    token,  'x-rapidapi-host': "alpha-vantage.p.rapidapi.com"
    }

  def get_currency_exchange_rate(self, msg):
    params = msg.split()
    params_len = len(params)
    to_curr, from_curr = "TRY", "USD"
    if params_len == 1:
      to_curr, from_curr = "TRY", "USD"
    elif params_len == 2:
      to_curr, from_curr = "TRY", params[1]
    else:
      to_curr, from_curr = params[2], params[1]

    querystring = {"function":"CURRENCY_EXCHANGE_RATE","to_currency":to_curr,"from_currency":from_curr}
    res = requests.request("GET", self.base_url, headers=self.headers, params=querystring)
    json_data = json.loads(res.text)

    from_code = json_data['Realtime Currency Exchange Rate']['1. From_Currency Code']
    to_code = json_data['Realtime Currency Exchange Rate']['3. To_Currency Code']
    ex_rate = json_data['Realtime Currency Exchange Rate']['5. Exchange Rate']

    return from_code + '/' + to_code + ':\t' + ex_rate


