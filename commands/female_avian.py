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
    "C": "cloud",
    "E": "echo"
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
    "a": "spirit",
    "ra": "caller",
    "ia": "keeper",
    "la": "singer",
    "na": "guardian",
    "li": "scout",
    "ri": "friend",
    "i": "melody",
    "va": "wanderer",
    "lyn": "heart",
    "ya": "dreamer",
    "sha": "listener",
    "sia": "storyteller",
}

extra = ["", "", "", "r", "l", "v", "th", "n"]

def generate_avian():
    start = random.choice(list(starts.keys()))
    middle = random.choice(list(middles.keys()))
    end = random.choice(list(ends.keys()))

    name = start + middle + random.choice(extra) + end
    meaning = f"The {middles[middle]} {ends[end]} of {starts[start]}"

    return name, meaning


def setup(bot):
    @bot.command()
    async def female_avian(ctx):
        name, meaning = generate_avian()

        result = (
            f"🪶 **Avian Name Generator**\n\n"
            f"**Name:** {name}\n"
            f"**Meaning:** {meaning}"
        )

        await ctx.send(result)
