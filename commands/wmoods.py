import random

moods = [
    "Calm",
    "Content",
    "Neutral",
    "Focused",
    "Curious",
    "Tired",
    "Relaxed",
    "Happy",
    "Joyful",
    "Playful",
    "Excited",
    "Energetic",
    "Affectionate",
    "Grateful",
    "Hopeful",
    "Inspired",
    "Playful-chaotic",
    "Sad",
    "Lonely",
    "Anxious",
    "Nervous",
    "Uncertain"
    "Overwhelmed",
    "Restless",
    "Guilt-touched",
    "Sensitive",
    "Angry",
    "Frustrated",
    "Agitated",
    "Defensive",
    "Distracted",
    "Conflicted",
    "Shaken",
    "Panicked",
    "Volatile",
    "Overstimulated"
]

def setup(bot):
    @bot.command()
    async def wmoods(ctx):
        result = (
            f"## The current moods in the warehouse\n"
            f"**Zevryn** is {random.choice(moods)}\n"
            f"**Quin** is {random.choice(moods)}\n"
            f"**Silk** is {random.choice(moods)}\n"
            f"**Nyx** is {random.choice(moods)}\n"
            f"**Dr. Sevka** is {random.choice(moods)}\n"
            f"**Ashara** is {random.choice(moods)}\n"
            f"**Ithindril** is {random.choice(moods)}"
        )
        await ctx.send(result)
