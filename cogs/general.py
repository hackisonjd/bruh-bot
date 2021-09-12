from discord.ext import commands
import random
import discord
import datetime

class General(commands.Cog):
  #general use commands

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='ping', brief="Responds to a ping command")
  @commands.has_permissions(administrator=True)
  async def ping(self, ctx):
    await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

  @commands.command(name='8ball', brief="Predicts your future")
  async def _8ball(self, ctx, *, question):
    responses = ["does will make his own mead?", 
                 "yeh", 
                 "ye", 
                 "holy fucking shit, yes", 
                 "does arkaj hate karn?", 
                 "sure", 
                 "yes. consider not asking again", 
                 "is wesley a sussy baka?", 
                 "does justin do a bit of trolling?", 
                 "yes dumbass", 
                 "eh, idk man", 
                 "look man, im not saying yes, but im not saying no", 
                 "how the hell am i supposed to know?", 
                 "bruh, i honestly don't know", 
                 "i'll have my answer once spencer finishes his toast","haha, no", 
                 "lol fuck no", 
                 "ni", 
                 "lul", 
                 "no fuckass"]

    embed = discord.Embed(
      title=f"{ctx.author.display_name}'s question: {question}",
      description=f'Here is your answer: {random.choice(responses)}',
      timestamp=datetime.datetime.utcnow(),
      color=discord.Color.darker_gray()
    )
    embed.set_thumbnail(url="https://www.vermontcountrystore.com/ccstore/v1/images/?source=/file/v436715391556442924/products/51327.main.png&height=300&width=300")
    await ctx.send(embed=embed)
    

  