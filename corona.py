import requests
import json
from prettytable import PrettyTable


class Corona:
  def __init__(self, token):
    self.base_url = "https://worldometers.p.rapidapi.com/api/coronavirus"
    self.headers = {
      "x-rapidapi-key": token,
      "x-rapidapi-host": 
      "worldometers.p.rapidapi.com",
      "useQueryString": "true"
    }

  def get_country_data(self, msg):
    country = "Turkey"
    params = msg.split()
    if len(params) >= 2:
      country = params[1]
    try:
      url = self.base_url + "/country/"+country
      res = requests.get(url, headers=self.headers)
      json_data = json.loads(res.text)

      t = PrettyTable(['Country', 'Active Cases', 'New Cases', 'New Deaths', 'Total Cases', 'Total Deaths'])

      data = json_data['data']
      t.add_row([data['Country'], data['Active Cases'], data['New Cases'], data['New Deaths'], data['Total Cases'], data['Total Deaths']])

      return "```\n"+str(t)+"\n```"
    except:
      return "Invalid Country!"
