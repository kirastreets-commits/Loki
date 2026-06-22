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


def generate_avian():
    start = random.choice(list(starts.keys()))
    middle = random.choice(list(middles.keys()))
    end = random.choice(list(ends.keys()))

    name = start + middle + end
    meaning = f"The {middles[middle]} {ends[end]} of {starts[start]}"

    return name, meaning


def setup(bot):
    @bot.command()
    async def male_avian(ctx):
        name, meaning = generate_avian()

        result = (
            f"🪶 **Avian Name Generator**\n\n"
            f"**Name:** {name}\n"
            f"**Meaning:** {meaning}"
        )

        await ctx.send(result)
