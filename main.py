from discord.ext import commands
import discord
from os import getenv
from dotenv import load_dotenv
import requests
import json
from alivinator import keep_alive
from cogs import minecraft, general, moderation

citizens = ["jackson", "jay", "spencer", "wesley", "justin", "@hackisonjd#1273", "@Noother#0459", "@wesleyywatson#4282", "@JayFourJustin#0946"]

kiryuchan = ["majima", "goro"]
majima_responses = ["KIRYU-CHAN!", ":musical_note: Sunao ni I LOVE YOU!\nTodokeyou kitto\nYOU LOVE ME!\nTsutawaru sa kimi ni\nniau garasu no\nkutsu wo sagasou\n\nFutari de STEP & GO!\nItsu made mo\nshinya juuni-ji wo\nsugitatte bokura no\nrabu majikku wa\ntoke wa shinai~ :musical_note:"]

class Bruh:
  def __init__(self):
    #Fetch discord bot token and set command prefix
    self.token = getenv('TOKEN')

    self.bot = commands.Bot(command_prefix='b:', case_insensitive=True)

    self.cogs = [
      {'name': 'Minecraft', 'obj': minecraft.Minecraft, 'active': True},
      {'name': 'General', 'obj': general.General, 'active': True},
      {'name': 'Moderation', 'obj': moderation.Moderation, 'active': True}
    ]

    self.add_events()
    self.init_cogs()

  def init_cogs(self):
    #Go through all cogs and add them to the bot 
    for cog in self.cogs:
      self.bot.add_cog(cog['obj'](self.bot))
  
  def add_events(self):
    self.bot.event(self.on_ready)

  async def on_ready(self):
    await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("cave1.ogg"))
    print(f'{self.bot.user.name} has successfully connected to Discord!')

  


  def start_bot(self):
    self.bot.run(self.token)

keep_alive()

if __name__ == '__main__':
  # Load env variables
  load_dotenv('.env')

  # Initialize bruh bot 
  b = Bruh()

  # Start the bruh bot 
  print("Starting the bruh sequence.")
  b.start_bot()

'''def get_insult():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
  json_data = json.loads(response.text)
  insult = json_data['insult']
  return(insult)

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$bruh'):
    await message.channel.send('sup fuckass')
  elif message.content.startswith('$insult'):
    insult = get_insult()
    await message.channel.send(insult)

  if any(word in str(message.content).lower() for word in citizens):
    await message.channel.send('Ah yes, a citizen of the District of Cocks.')

  if any(word in str(message.content).lower() for word in kiryuchan):
    await message.channel.send(random.choice(majima_responses))

  
'''
