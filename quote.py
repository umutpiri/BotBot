import requests
import json


class Quote:
  def __init__(self):
    self.base_url = "https://zenquotes.io/api"
  
  def get_random(self):
    url = self.base_url + '/random'
    response = requests.get(url)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote