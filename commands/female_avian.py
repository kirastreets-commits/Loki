import random

starts = [
    "Qu", "K", "T", "S", "V",
    "L", "R", "W", "N", "C", "E"
]

middles = [
    "i", "e", "a", "ae",
    "ai", "y", "o", "i"
]

ends = [
    "a", "ra", "ia", "la",
    "na", "li", "ri", "i"
]

def setup(bot):
    @bot.command()
    async def female_avian(ctx):
        result = random.choice(starts) + random.choice(middles) + random.choice(ends)
        await ctx.send(result)
