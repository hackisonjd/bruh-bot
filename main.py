from discord.ext import commands
import discord
from os import getenv
from dotenv import load_dotenv
import requests
import json
from alivinator import keep_alive
from cogs import minecraft, general, moderation

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

  async def on_message(self, message):
    if message.author == self.bot.user:
      return message

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

