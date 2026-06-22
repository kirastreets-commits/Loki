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
    "a toothbrush",
    "a hairbrush",
    "a favorite mug",
    "a gaming controller",
    "a notebook",
    "a hoodie",
    "a stuffed animal",
    "a collection of shiny rocks",
    "a pair of headphones",
    "a hat",
    "a wallet",
    "a set of keys",
    "a deck of cards",
    "a coffee cup",
    "a half-finished project",
    "an entire chair",
    "a lamp",
    "an important-looking button",
    "a mysterious box",
    "a bag that definitely wasn't theirs",
    "a very expensive piece of equipment",
    "a sign warning people not to steal things",
    "someone else's stolen goods",
    "an entire pile of blankets",
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
    "refuse to give it back unless the victim apologises for a perceived indiscretion (this is revenge)",
    "roll onto their back and demand belly rubs instead",
    "attempt to distract the victim with cuddles",
    "make tiny sad noises until the victim feels guilty",
    "pretend they have no idea what anyone is talking about",
    "offer emotional support instead of returning the item",
    "hide behind Ashara",
    "hide behind Zevryn",
    "look personally offended by the accusation",
    "have already hidden it somewhere else",
    "immediately flee the scene",
    "try to steal something else while everyone is distracted",
    "claim it was abandoned property",
    "insist they found it fair and square",
    "declare it part of their hoard",
    "refuse to acknowledge reality",
    "attempt to negotiate visitation rights",
    "curl protectively around it and growl",
    "add it to their nest while maintaining eye contact",
    "have buried it beneath a pile of blankets",
    "have fallen asleep on top of it",
    "have claimed it as nesting material",
    "have groomed it extensively",
    "are guarding it like a dragon guards treasure",
    "have accidentally broken it and are hoping nobody notices",
    "already traded it to someone else",
    "claim they were keeping it safe",
    "have somehow stolen three more things in the meantime",
    "challenge the victim to a duel for ownership",
    "offer a completely unrelated item as compensation",
    "have hidden it in an absurdly obvious location"
]
victim_reaction = [
    "The victim is not amused.",
    "The victim seems oddly unsurprised.",
    "This is apparently not the first time this week.",
    "Everyone else immediately knows who the culprit is.",
    "The warehouse enters a state of chaos.",
    "Nobody is willing to help recover the item.",
    "This somehow becomes Zevryn's problem.",
    "Ashara thinks this is hilarious.",
    "Ender starts recording the incident.",
    "Silk is already taking bets on the outcome.",
    "Sevka is takes notes curiously.",
    "Nyx is questioning his life choices.",
    "The thief is very proud of themselves.",
    "The thief has absolutely no regrets."
]
def setup(bot):
    @bot.command()
    async def theft(ctx):

        result = (
            f"**{random.choice(thief)}** stole "
            f"{random.choice(item)} from "
            f"**{random.choice(victim)}**. "
            f"When confronted, they {random.choice(react)}. "
            f"{random.choice(victim_reaction)}"
        )

        await ctx.send(result)
