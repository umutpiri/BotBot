import random

HEADS = "██╗░░██╗███████╗░█████╗░██████╗░░██████╗\n██║░░██║██╔════╝██╔══██╗██╔══██╗██╔════╝\n███████║█████╗░░███████║██║░░██║╚█████╗░\n██╔══██║██╔══╝░░██╔══██║██║░░██║░╚═══██╗\n██║░░██║███████╗██║░░██║██████╔╝██████╔╝\n╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░╚═════╝░"
TAILS = "████████╗░█████╗░██╗██╗░░░░░░██████╗\n╚══██╔══╝██╔══██╗██║██║░░░░░██╔════╝\n░░░██║░░░███████║██║██║░░░░░╚█████╗░\n░░░██║░░░██╔══██║██║██║░░░░░░╚═══██╗\n░░░██║░░░██║░░██║██║███████╗██████╔╝\n░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚══════╝╚═════╝░"

class Gamble:
  def coin_flip(self):
    rand_num = random.randint(1, 2)
    if rand_num == 1:
      return HEADS
    else:
      return TAILS

  def get_random_number(self, msg):
    params = msg.split()
    params_len = len(params)
    start = 1
    end = 10
    try:
      if params_len == 1:
        return random.randint(start, end)
      elif params_len == 2:
        end = int(params[1])
        return random.randint(start, end)
      else:
        num1 = int(params[1])
        num2 = int(params[2])
        start = min(num1, num2)
        end = max(num1, num2)
        return random.randint(start, end)
    except:
      return "Invalid input"