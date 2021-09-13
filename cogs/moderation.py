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

  @commands.command(name='mute', brief='Mutes a user')
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, member : discord.Member, *, reason=None):
    guild = ctx.guild
    default_role = discord.utils.get(guild.roles, name="member")
    muted_role = discord.utils.get(guild.roles, name="mute")

    await member.add_roles(muted_role, reason=reason)
    await member.remove_roles(default_role)
    await ctx.channel.send("Muted {0} for {1}".format(member.mention, reason))
    await member.send("You were muted in Jackson's Dank Server you fucking idiot.")

  @commands.command(name='unmute', brief='Unmutes a user.')
  @commands.has_permissions(administrator=True)
  async def unmute(self, ctx, member: discord.Member):
    guild = ctx.guild
    default_role = discord.utils.get(guild.roles, name="member")
    muted_role = discord.utils.get(guild.roles, name="mute")

    await member.remove_roles(muted_role)
    await member.add_roles(default_role)
    await ctx.channel.send("Unmuted {0}".format(member.mention))

  @commands.command(name='kick', brief='Kicks a user from the server')
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

  @commands.command(name='ban', brief='Bans a user from the server')
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)


  