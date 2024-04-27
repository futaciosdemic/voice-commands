import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

client = commands.Bot(command_prefix='!', intents=intents) # this is the prefix u can change it whenever u want(u can change the client also)

@client.command()
async def mute(ctx):
    if ctx.author.voice:
        await ctx.author.edit(mute=True)
        await ctx.send("You have been muted")
    else:
        await ctx.send("You are not in a voice channel")

@client.command()
async def unmute(ctx):
    if ctx.author.voice:
        await ctx.author.edit(mute=False)
        await ctx.send("You have been unmuted")
    else:
        await ctx.send("You are not in a voice channel")

@client.command()
async def deafen(ctx):
    if ctx.author.voice:
        await ctx.author.edit(deafen=True)
        await ctx.send("You have been deafened")
    else:
        await ctx.send("You are not in a voice channel")

@client.command()
async def undeafen(ctx):
    # Check if the user is in a voice channel
    if ctx.author.voice:
        # Undeafen the user
        await ctx.author.edit(deafen=False)
        await ctx.send("You have been undeafened.")
    else:
        await ctx.send("You are not in a voice channel.")
