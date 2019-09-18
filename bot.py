import discord
from discord.ext import commands
import cmds

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0] .strip()

token = read_token()

cmds.bot.run(token)
