import discord
import threading
import time

MAX_SECONDS = 7200  # 2 Hours

def secs_to_hhmmss(seconds):
  hours = seconds // (3600)
  seconds %= (3600)
  minutes = seconds // 60
  seconds %= 60
  return "%02i:%02i:%02i" % (hours, minutes, seconds)


class Timer:
  def __init__(self, msg, channel=None):
    params = msg.split()
    params_len = len(params)

    time_sec = 60
    title = "Timer"

    if params_len == 3:
      if params[1].isnumeric():
        time_sec = int(params[1])
        title = params[2]
      elif params[2].isnumeric():
        time_sec = int(params[2])
        title = params[1]
    if params_len == 2:
      if params[1].isnumeric():
        time_sec = int(params[1])
      else:
        title = params[1]

    if time_sec > MAX_SECONDS:
      time_sec = MAX_SECONDS

    self.time=time_sec
    self.channel = channel
    self.title = title
  
  async def start_timer(self):
    embed = discord.Embed(title=self.title, description= "Remaining time\n" + secs_to_hhmmss(self.time))

    self.msg = await self.channel.send(embed=embed)

    self.thread = threading.Thread(target=await self.update_timer())
    self.thread.start()

  async def update_timer(self):
    is_finished = False
    while not is_finished:
      time.sleep(1)

      self.time -= 1

      if self.time <= 0:
        embed = discord.Embed(title=self.title, description= "TIME IS UP!")
        is_finished = True
      else:
        embed = discord.Embed(title=self.title, description= "Remaining time\n" + secs_to_hhmmss(self.time))
      
      await self.msg.edit(embed=embed)

      

