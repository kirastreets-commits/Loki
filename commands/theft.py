import random

thief = ["Quin", "Ithindril" ]
item = ["snacks", 
    "a single sock", 
    "underwear", 
    "shoes",
    "a sex toy", 
    "a phone", 
    "a piece of paper with something written on it", 
    "a photo",
    "a shirt",
    "pants or a skirt",
    "something from the victims nest or sleep area",
    "money",
    "drugs",
    "jewelry",
    "a handwritten letter",
    "a favorite weapon",
    "a cloak or jacket that smells like the owner",
    "a potion",
    "the victim’s 'lucky' item or clothes",
    "half eaten food (when the victim looked away for a second)",
    "a blanket that smells like the owner",
    "a pillow",
]
victim = ["Zevryn",  
    "Silk", 
    "Dr.Sevka", 
    "Ashara",
    "Nyx",
    "Ender"
]
react = [
    "bite at every attempt to take it back",  
    "whine, beg and use puppy dog eyes that pull at the heart strings", 
    "sit on it in an attempt to keep it", 
    "have licked it and it's noticeably wet",
    "look guilty and there is a piece missing (whether it was eaten or torn it's unclear)",
    "refuse to let the victim leave and try to trap them in their nest",
    "refuse to help but it's hidden somewhere in their nest",
    "wont relinquish it unless they get something in return",
    "are laying under it and look very comfortable",
    "stick it in their mouth and stare as if nothing happened",
    "refuse to give it back unless the victim apologises for a perceived indiscretion (this is revenge)"
]

def setup(bot):
    @bot.command()
    async def theft(ctx):

        result = (
            f"{random.choice(thief)} stole "
            f"{random.choice(item)} from "
            f"{random.choice(victim)}. "
            f"When confronted, they {random.choice(react)}."
        )

        await ctx.send(result)