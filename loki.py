import discord
from discord.ext import commands

from commands import theft, prompt, dragon, dragonmood, ith, ash, zev, quin, male_avian

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)



@bot.event
async def on_ready():
    print(f"🐉 Sanctuary is online as {bot.user}")

theft.setup(bot)
prompt.setup(bot)
dragon.setup(bot)
dragonmood.setup(bot)
ith.setup(bot)
ash.setup(bot)
zev.setup(bot)
quin.setup(bot)
male_avian.setup(bot)

import os

bot.run(os.getenv("DISCORD_TOKEN"))
