import requests
import json


class Gif:
  def __init__(self, token):
    self.base_url = "https://api.giphy.com/v1"
    self.token = token
  
  def get_random(self):
    url = self.base_url + '/gifs/random?api_key=' + self.token

    res = requests.get(url)
    json_data = json.loads(res.text)

    return json_data['data']['images']['downsized_large']['url']
  