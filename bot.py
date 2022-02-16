import datetime

import discord
from discord.ext import commands

bot = commands.Bot("!")


@bot.event
async def on_ready():
    print(f"Estou pronto! Estou conectado como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "palavrao" in message.content:
        await message.channel.send(
            f"Por favor, {message.author.name}, nao ofenda os demais usuarios!"
        )

        await message.delete()

    await bot.process_commands(message)

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)

bot.run("OTQzNjA3ODAyODc2Nzg4NzU3.Yg1hPw.OGljPYp6KS45K6YvNJgr8rgHIhI")