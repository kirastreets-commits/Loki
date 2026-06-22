import random

en = [
    "working on a new invention",
    "repairing damaged equipment",
    "writing code for a new project",
    "debugging a particularly stubborn issue",
    "testing a prototype",
    "upgrading the warehouse systems",
    "monitoring security feeds",
    "reviewing system diagnostics",
    "building something nobody else understands",
    "working on a secret project",
    "completely losing track of time while working",
    "focused so intensely on a project that he forgot lunch",
    "surrounded by tools and spare parts",
    "staring at a screen with intense concentration",
    "making notes for a future project",
    "researching new technology",
    "working through a list of ideas",
    "trying to solve a problem that nobody asked him to solve",
    "optimizing something that already worked fine",
    "disappearing into a project rabbit hole",
    "keeping everything running behind the scenes",
    "listening to Quin talk excitedly about something",
    "watching Ashara cause problems from a safe distance",
    "helping Sevka with a project",
    "having a discussion with Zevryn",
    "being dragged into one of Silk's schemes",
    "checking in on the gang",
    "helping someone with a personal project",
    "trying to be productive despite constant interruptions",
    "quietly enjoying everyone's company",
    "trying to work while Ithindril sits on his keyboard",
    "being used as a pillow by Ashara",
    "searching for a tool Ithindril stole",
    "attempting to recover stolen equipment",
    "trying to explain why electronics shouldn't be licked",
    "discovering that Ashara moved something important",
    "trying to keep dragons out of sensitive equipment",
    "accepting that the dragons own the warehouse now",
    "cleaning fur, scales, and feathers out of machinery",
    "reviewing reports of magical creature sightings",
    "designing equipment for rescue missions",
    "analyzing data from recent rescues",
    "maintaining rescue equipment",
    "testing tracking technology",
    "helping coordinate rescue efforts",
    "watching tech videos",
    "reading about new inventions",
    "drinking coffee while reviewing projects",
    "taking a rare break",
    "watching the warehouse activity from his workstation",
    "listening to music while he works",
    "enjoying a quiet moment",
    "organizing his workbench",
    "actually getting some sleep for once",
    "wondering where all his tools keep disappearing to",
    "finding yet another dragon in a place dragons shouldn't fit",
    "trying to remember what he originally started working on",
    "holding together a project with determination and optimism",
    "being interrupted for the seventh time today",
    "explaining the same thing for the third time",
    "pretending everything is under control",
    "wondering why every project becomes more complicated",
    "is asleep at his desk with a dragon curled on top of him",
    "has discovered a problem before it became a disaster",
    "has finally found the thing Ithindril stole three weeks ago",
    "is being aggressively supervised by Ashara",
    "is testing something that definitely won't explode (probably)",
    "is wondering how he became responsible for all of this"

]

def setup(bot):
    @bot.command()
    async def ender(ctx):

        result = (
            f"*Ender is currently {random.choice(en)}*."
        )

        await ctx.send(result)