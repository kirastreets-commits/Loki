import random

aquiny = [
    "raiding someone's things for snacks",
    "curled up in one of his nests sleeping",
    "curled up in one of his nests eating snacks",
    "listening to Ender talk about tech",
    "reading up on the latest tech news",
    "gliding around the warehouse",
    "playing with Ithindril",
    "watching his monitoring system on his phone with a sad expression",
    "singing a threadsong - it's a beautiful sound",
    "singing a threadsong - it feels sad",
    "building a new nest out of random soft objects",
    "rearranging his nest for the third time today",
    "hoarding shiny objects 'just in case',
    "tangled in blankets refusing to move",
    "half-asleep but still talking",
    "guarding his snack pile like it’s sacred",
    "humming softly while fixing his nest feathers",
    "falling asleep mid-sentence",
    "talking to three people at once and forgetting what he said",
    "pacing in circles while explaining something exciting",
    "interrupting himself with a new idea mid-sentence",
    "attempting five tasks and completing none",
    "chasing a thought like it physically ran away",
    "dramatically reenacting something that happened five minutes ago",
    "vibrating with excitement about literally nothing specific",
    "trying to teach someone something while also forgetting how it works",
    "humming old flock songs he barely remembers",
    "translating emotions into chirp patterns",
    "teaching one of the gang how windcalls 'feel'",
    "singing a threadsong to calm himself down",
    "sitting in the middle of everyone just listening happily",
    "trying to “fix” someone’s mood by talking too much",
    "arguing playfully with Zevryn about snacks",
    "arguing playfully with Ender about snacks",
    "arguing playfully with Nyx about snacks",
    "bothering Sevka with endless questions",
    "helping Ithindril with something but getting distracted halfway",
    "helping Nyx with something but getting distracted halfway",
    "helping Ender with something but getting distracted halfway",
    "asking Ender what every button does",
    "clicking things he shouldn’t (again)",
    "getting distracted by glowing interfaces",
    "organizing data “based on vibes” instead of logic",
    "trying to sing at a computer to “make it work faster (helping Ender)”,
    "sitting quietly after overstimulation",
    "missing someone but not saying it",
    "replaying memories through threadsong",
    "resting his head against someone’s shoulder without speaking",
    "hiding snacks and forgetting where he put them",
    "insisting something happened that didn’t",
    "getting stuck in a nest and refusing to admit it",
    "trying to 'help' and making things worse",
    "declaring himself 'Snack Guardian' for the day",
]

def setup(bot):
    @bot.command()
    async def quin(ctx):

        result = (
            f"*Quin is currently {random.choice(aquiny)}*"
        )

        await ctx.send(result)
