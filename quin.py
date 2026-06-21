import random

aquiny = [
    "raiding someone's things for snacks",
    "curled up in one of his nests sleeping",
    "curled up in one of his nests eating snacks",
    "listening to Ender talk about tech",
    "reading up on the latest tech news",
    "gliding around the warehouse",
    "playing with Ithindril",
]

def setup(bot):
    @bot.command()
    async def quin(ctx):

        result = (
            f"*Quin is currently {random.choice(aquiny)}*"
        )

        await ctx.send(result)