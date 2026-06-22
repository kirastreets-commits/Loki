import random

ny = [
    "making another communal nest for everyone, taking just about every blanket, pillow, and piece of clothing possible",
    "Nyx chitters excitedly at finding new supplies. Fae stashes them in faer nest.",
    "Nyx is chasing Ithindril around. She's causing chaos again.",
    "Nyx has been in faer room all day tending to Ithindril. It's a bad day.",
    "Nyx is tracing faer tattoos anxiously, trying to focus faerself and get back on track with the day.",
    "Nyx has woken before anyone else. Fae decide to check in on the gang while they are all still asleep.",
    "Nyx is helping Dr. Sevka with producing more of the drugs that they sell.",
    "Nyx returns from being with a client. Fae seems tired.",
    "Nyx is making another communal nest for everyone, taking just about every blanket, pillow, and piece of clothing possible."
]

def setup(bot):
    @bot.command()
    async def nyx(ctx):

        result = (
            f"*Nyx is currently {random.choice(ny)}*."
        )

        await ctx.send(result)
