import discord
from discord.ext import commands

class Moderation(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='clear', brief='Purge a channel of messages')
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, amount=5):
    await ctx.channel.send("Clearing {0} messages!".format(amount))
    await ctx.channel.purge(limit=amount+1)

  @commands.command(name='kick', brief='Kicks a user from the server')
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

  @commands.command(name='ban', brief='Bans a user from the server')
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


  