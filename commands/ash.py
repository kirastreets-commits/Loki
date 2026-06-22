import random

# ----- ASHARA -----
ashara = [
    "hiding in her nest",
    "stealing something for her nest",
    "purring loudly",
    "eating someones snacks",
    "sleeping peacefully",
    "demanding attention loudly",
    "cuddling with Nyx",
    "cuddling with Zevryn",
    "cuddling with Quin",
    "cuddling with Ithindril",
    "cuddling with Sevka",
    "cuddling with Silk",
    "cuddling with Ender",
    "holding Quin hostage",
    "holding Silk hostage",
    "holding Nyx hostage",
    "holding Zevryn hostage",
    "holding Sevka hostage",
    "holding Ender hostage",
    "grooming Ender",
    "grooming Zevryn",
    "grooming Nyx",
    "grooming Quin",
    "grooming Silk",
    "leaving little burn marks on the floor because she's bored",
    "blowing hot air on Nyx because they annoyed her",
    "blowing hot air on Silk because they annoyed her",
    "blowing hot air on Ender because they annoyed her",
    "blowing hot air on Quin because they annoyed her",
    "blowing hot air on Ithindril because they annoyed her",
    "blowing hot air on Zevryn because they annoyed her",
    "blowing hot air on Sevka because they annoyed her",
    "playing with Ithindril in  the warehouse and making so much mess and noise",
    "growling loudly in warning",
    "fussing with her nest",
    "growling and huffing because she's hangry",
    "setting minor fires that Sevka keeps puttinng out",
    "scraping her claws on the ground loudly to get attention",
   
]

def setup(bot):
    @bot.command()
    async def ash(ctx):

        result = (
            f"*Ashara is currently {random.choice(ashara)}*."
        )

        await ctx.send(result)
