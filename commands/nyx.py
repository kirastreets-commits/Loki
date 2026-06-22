import random

ny = [
    "making another communal nest for everyone, taking just about every blanket, pillow, and piece of clothing possible"
]

def setup(bot):
    @bot.command()
    async def nyx(ctx):

        result = (
            f"*Nyx is currently {random.choice(ny)}*."
        )

        await ctx.send(result)