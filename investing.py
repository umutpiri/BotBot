import requests
import re
from prettytable import PrettyTable


def get_text_from_element(elem):
    start = elem.find('>') + 1
    end = elem.find('<', 2)
    return elem[start:end]


class Investing:
  def __init__(self):
    self.base_url = "https://www.investing.com"
    self.headers = {"User-Agent": "Mozilla/5.0"}
    
  def get_btc_usd(self, msg):
    # TODO: convert to dynamic func
    try:
      base = 'btc'


      url = self.base_url +"/crypto/bitcoin/"+base+"-usd"
      r = requests.get(url, headers=self.headers)
      html = r.text

      t = PrettyTable(['', 'Price', 'Change','5 Min', '15 Min', 'Hourly', 'Daily', 'Monthly'])

      summary_elements = re.findall(r'<td class="left[^<]*Font[^<]*>(?!Real)[^<]*<\/td>', html)
      technical_summary = []
      for element in summary_elements[-5:]:
          text = get_text_from_element(element)
          technical_summary.append(text)

      price_re = r'<span class="arial_26 inlineblock[^<]*<\/span>'
      change_perc_re = r'<span class="arial_20[^<]*%<\/span>'

      price_element = re.search(price_re, html).group()
      price = get_text_from_element(price_element)
      change_element = re.search(change_perc_re, html).group()
      change = get_text_from_element(change_element)
      t.add_row([base.upper(), price, change]+technical_summary)

      return "```\n"+str(t)+"\n```"
    except:
      return "Invalid parameter"
