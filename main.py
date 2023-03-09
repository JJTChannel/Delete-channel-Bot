from discord.ext import commands
import discord
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents = intents)
@bot.event
async def on_ready():
    print("ONLINE!")

@bot.command()
async def clean(ctx,name):
    await ctx.send(f"Deleting {name}!")
    for channel in bot.get_all_channels():
        if channel.name == name:
            await channel.delete()
    await("Deleted!")

bot.run("token")
