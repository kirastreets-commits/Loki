import random

starts = [
    "Qu", "K", "T", "S", "V",
    "L", "R", "W", "N", "C"
]

middles = [
    "i", "e", "a", "ae",
    "ai", "y", "o"
]

ends = [
    "n", "r", "l", "s",
    "th", "k", "yn"
]

def generate_avian_name():
    return random.choice(starts) + random.choice(middles) + random.choice(ends)

def setup(bot):
    @bot.command()
    async def male_avian(ctx):
        result = random.choice(starts) + random.choice(middles) + random.choice(ends)
        await ctx.send(result)