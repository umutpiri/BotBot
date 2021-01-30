import requests
import json
import random


class Gif:
  def __init__(self, token):
    self.base_url = "https://api.giphy.com/v1/gifs"
    self.token = token
  
  def get_random(self, msg):
    url = self.base_url + '/random'
    params = {"api_key": self.token}

    msg_split = msg.split(" ", 1)
    if len(msg_split) > 1:
      url = self.base_url + '/translate'
      weirdness = random.randint(0, 10)
      params['s'] = msg_split[1]
      params['weirdness'] = weirdness

    res = requests.get(url, params=params)
    json_data = json.loads(res.text)

    return json_data['data']['images']['downsized_large']['url']
  