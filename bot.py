import discord
from discord.ext import commands

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0] .strip()

token = read_token()

bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True) #search function
async def opgg(ctx, arg):
    await ctx.send("https://na.op.gg/summoner/userName="+arg)

#stats function - create op.gg API and pull winrate and preferred role.



bot.run(token)
