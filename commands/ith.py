import random

# ----- ITHINDRIL -----
ithindril = [
    "hiding in her nest",
    "hiding in someones clothes",
    "sneaking around",
    "stealing something for her nest",
    "purring loudly",
    "eating someones snacks",
    "sleeping peacefully",
    "begging for attention",
    "demanding attention",
    "cuddling with Nyx",
    "cuddling with Zevryn",
    "cuddling with Quin",
    "cuddling with Ashara",
    "cuddling with Sevka",
    "cuddling with Silk",
    "cuddling with Ender",
    "licking Nyx's face",
    "licking Zevryn's face",
    "licking Quins's face",
    "dashing around the warehouse with a dose of the zoomies",
    "holding Quin hostage",
    "holding Silk hostage",
    "holding Nyx hostage",
    "holding Zevryn hostage",
    "holding Sevka hostage",
    "grooming Ashara",
    "grooming Zevryn",
    "grooming Nyx",
    "grooming Quin",
    "curled up on Silk's lap and refusing to budge",
    "celebrating stolen goods with Quin",
    "eating something she shouldn't be"
   
]


def setup(bot):
    @bot.command()
    async def ith(ctx):

        result = (
            f"*Ithindril is currently {random.choice(ithindril)}*"
        )

        await ctx.send(result)