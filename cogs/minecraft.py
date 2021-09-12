import discord
from discord.ext import commands
from os import getenv
from mcstatus import MinecraftServer
from mcrcon import MCRcon
import datetime

class Minecraft(commands.Cog):
  # Minecraft specific commands

  def __init__ (self, bot):
    self.bot = bot

    # variable collection
    self.host = getenv('SERVER_IP')
    self.query_port = int(getenv('QUERY_PORT'))
    self.rcon_port = int(getenv('RCON_PORT'))
    self.rcon_pwd = getenv('RCON_PASSWORD')

    # endpoint intialization
    self.query_server = MinecraftServer(self.host, self.query_port)

  @commands.command(name='status', brief="Check the Minecraft server's status")
  async def status(self, ctx):
    # load server status using MinecraftServer api
    status = self.query_server.status()
    #query = self.query_server.query()

    embed = discord.Embed(
      title="Jay's Minecraft Server Info",
      description="Jay's Minecraft Server has {0} players online and replied back to me in {1} ms".format(status.players.online, round(status.latency)),
      color=discord.Color.orange(),
      timestamp=datetime.datetime.utcnow()
    )
    embed.set_thumbnail(url="https://i.pinimg.com/originals/68/64/a3/6864a38e077516430e38b5eed4ffef56.png")

    await ctx.send(embed=embed)

  @commands.command(name='msg', brief="Message the server or a player.")
  @commands.has_permissions(administrator=True)
  async def msg(self, ctx, msg=None, player=None):
    # message the server or someone specific
    if player is None:
      with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
        mcr.command(f"say {msg}")
        await ctx.channel.send(f"Messaged Minecraft server")
    else:
      with MCRcon(host=self.host, password=self.rcon_pwd, port=self.rcon_port) as mcr:
        resp = mcr.command(f"tell {player} {msg}")
        await ctx.channel.send(f"Server response: {resp}")