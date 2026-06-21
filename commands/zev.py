import random


zevryn = [
    "cuddling with Ashara in her nest",
    "polishing and cleaning his weapons",
    "training in his training room",
    "going through a slow set of martial arts moves",
    "sitting cross-legged, his eyes closed, apparently meditating on something", 
    "discussing plans with the gang",
    "having a private chat with Silk",
    "having a private chat with Dr. Sevka",
    "having a private chat with Ender",
    "out on a job to save some magical creatures",
    "trying to soothe a moody Ashara",
    "testing a new weapon technique",
    "repairing damage to his armor",
    "reviewing recordings from past missions",
    "working through a difficult combat exercise",
    "training while carrying extra weights",
    "stretching after a long training session",
    "reviewing mission reports",
    "planning future rescue operations",
    "checking in on everyone's wellbeing",
    "organizing equipment for the next job",
    "updating emergency response plans",
    "tracking reports of magical disturbances",
    "preparing supplies for a rescue mission",
    "investigating a creature sighting",
    "watching the sunrise from a rooftop",
    "reading an old martial arts manuscript",
    "drinking tea in silence",
    "sitting quietly beside Ashara",
    "staring out a window, lost in thought",
    "listening to the sounds of the warehouse",
    "helping Ender move some heavy equipment",
    "reluctantly allowing Ashara to fuss over him",
    "sharing a meal with the gang",
    "listening patiently while someone vents",
    "checking on Silk after a difficult day",
    "helping Dr. Sevka transport supplies",
    "watching one of Ender's latest projects",
    "breaking up a minor argument before it escalates",
    "being dragged into a group activity against his better judgment",
    "quietly making sure everyone gets home safely",
    "being used as a pillow by Ashara",
    "trying and failing to relax",
    "pretending he doesn't enjoy the attention he's getting",
    "staring at a complicated piece of technology Ender handed him",
    "wondering how the gang keeps finding trouble",
    "looking mildly concerned about something only he noticed",
    "questioning his life choices after agreeing to help with a project"
]

def setup(bot):
    @bot.command()
    async def zev(ctx):

        result = (
            f"*Zevryn is currently {random.choice(zevryn)}*"
        )

        await ctx.send(result)
