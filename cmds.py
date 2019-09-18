import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='!')

@bot.command(pass_context=True)
async def opgg(ctx, arg):
    """
    searches summer name input
    returns hyperlink of the summoner.
    """
    await ctx.send("https://na.op.gg/summoner/userName="+arg)

# stats function - create op.gg API and pull
# summoner name, winrate, and preferred role.
# async def stats()

