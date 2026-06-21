import random


zevryn = [
    "cuddling with Ashara in her nest",
    "polishing and cleaning his weapons",
    "training in his training room",
    "going through a slow set of martial arts moves",
    "sitting cross-legged, his eyes closed, apparently meditating on something" 
    "discussing plans with the gang",
    "having a private chat with Silk",
    "out on a job to save some magical creatures",
    "trying to soothe a moody Ashara",
]

def setup(bot):
    @bot.command()
    async def zev(ctx):

        result = (
            f"*Zevryn is currently {random.choice(zevryn)}*"
        )

        await ctx.send(result)