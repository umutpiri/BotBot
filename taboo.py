from prettytable import PrettyTable
import random
from replit import db


class Taboo:
  def __init__(self):
    self.keys = db.keys()

  def get_random(self, msg):
    k = 5

    try:
      k = int(msg.split()[1])
      if k > 7:
        k = 5
    except:
      k = 5

    keys = random.choices(list(self.keys), k=k)

    t = PrettyTable(keys)
    values = []

    for key in keys:
      forbidden = db[key]
      values.append(forbidden.replace(',', '\n'))
    
    t.add_row(values)
    t.min_width = 20

    return "```\n```\n"+str(t)+"\n```\n```"