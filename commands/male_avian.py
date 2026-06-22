import random

starts = {
    "Qu": "song",
    "K": "wind",
    "T": "flight",
    "S": "sky",
    "V": "journey",
    "L": "light",
    "R": "river",
    "W": "wander",
    "N": "nest",
    "C": "cloud"
}

middles = {
    "i": "small",
    "e": "gentle",
    "a": "strong",
    "ae": "ancient",
    "ai": "curious",
    "y": "free",
    "o": "bright"
}

ends = {
    "n": "spirit",
    "r": "caller",
    "l": "keeper",
    "s": "singer",
    "th": "guardian",
    "k": "scout",
    "yn": "friend"
}

start = random.choice(list(starts.keys()))
middle = random.choice(list(middles.keys()))
end = random.choice(list(ends.keys()))

name = start + middle + end
meaning = f"{starts[start]} {middles[middle]} {ends[end]}"

def setup(bot):
    @bot.command()
    async def male_avian(ctx):
        result = (
        f"Name: {name} \n"
        f"Meaning: The {middles[middle]} {ends[end]} of {starts[start]}"
        )
        
        await ctx.send(result)
