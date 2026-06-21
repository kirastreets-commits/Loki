import random

aquiny = [
    "raiding someone's things for snacks",
    "curled up in one of his nests sleeping",
    "curled up in one of his nests eating snacks",
    "listening to Ender talk about tech",
    "reading up on the latest tech news",
    "gliding around the warehouse",
    "playing with Ithindril",
    "watching his monitoring system on his phone with a sad expression",
    "singing a threadsong - it's a beautiful sound",
    "singing a threadsong - it feels sad",
]

def setup(bot):
    @bot.command()
    async def quin(ctx):

        result = (
            f"*Quin is currently {random.choice(aquiny)}*"
        )

        await ctx.send(result)
