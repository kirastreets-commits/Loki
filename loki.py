import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

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
# ----- NAME D -----
charD = [
    "Zevryn", "Quin", "Silk", "Dr. Sevka", "Ashara"
]


# ----- NAME L -----
charL = [
    "Nyx", "Ender", "Ithindril"
]

# ----- Problem -----
prob = [
    "Missing or stolen item", 
    "Someone sick or injured", 
    "Magic causes problems", 
    "Sevka's experiment goes wrong", 
    "emergency: magical creature in danger", 
    "Outlaw hunters find one of them", 
    "Something from one of the characters backgrounds comes back to haunt them", 
    "they get trapped", "something got hacked", "someone's magic becomes unstable", 
    "an explosion", "flooding", "a job goes wrong", "hiding something from one of the crew", 
    "they get separated from the crew",
    "someone loses their memory temporarily somehow",
    "accidentally walking in on something embarassing",
    "one member hides an injury or problem",
    "one member becomes distant and withdrawn",
    "a secret is accidentally revealed",
    "one member hides an injury or problem",
    "cultural differences causes a problem or misundersatnding",
    "Someone from the crew’s past returns unexpectedly",
    "a blackout or magical disruption causes chaos",
    "the crew is blamed for something they didn’t do",
    "a magical creature escapes into a populated area"
]

# ----- MOOD -----
mood = [
    "hurt/comfort", 
    "bonding", 
    "conflict", 
    "angst", 
    "romance", 
    "danger", 
    "injury", 
    "protectiveness", 
    "pining", 
    "touch starved", 
    "cosy", 
    "fear", 
    "love", 
    "betrayal", 
    "fluff", 
    "family", 
    "anger", 
    "sadness", 
    "jealousy", 
    "revenge"
]

# ----- RANDOM THING TO INCLUDE -----
thing = [
    "Snacks", 
    "Drugs", 
    "Money", 
    "a magical creature", 
    "police or authorities", 
    "a nest", 
    "fire", 
    "a confession", 
    "bad weather", 
    "water", 
    "rain",  
    "broken item", 
    "a piece of backstory", 
    "a compliment", 
    "a lie", 
    "music", 
    "a hobby", 
    "a secret",
    "a magic poion",
    "Ender's new experimental tech",
    "one of Zevryn's weapons",
    "a meal",
    "Zevryn cooking them food",
    "a part of their culture",
    "a gift",
    "someone's odd nesting behaviour"
]

# ----- DRAGON SPECIES -----
species = [
    "Western Dragon", 
    "Eastern Dragon", 
    "Western Pygmy", 
    "Eastern Pygmy",
    "Wyvern Pygmy",
    "Wyvern"
]
# ----- MAGIC -----
magic = [
    "Fire", 
    "Earth", 
    "Water", 
    "Air"
]

# ----- COLOUR -----
colour = [
    "White", 
    "Black", 
    "Red", 
    "Blue", 
    "Green", 
    "Purple", 
    "Yellow",
    "Orange", 
    "Pink"
]

# ----- PERSONALITY -----
perso = [
    "Quiet and thoughtful",
    "Arrogant but loyal",
    "Playful and chaotic",
    "Wise and ancient",
    "Curious and adventurous",
    "Melancholic and distant",
    "Protective and fierce"
]

# ----- TRAIT -----
trait = [
    "Glowing eyes",
    "Cracked horns",
    "Prominant scar",
    "Leaks magic in breath",
    "Iridescent or shimmering scales",
    "Extra large",
    "Extra small (runt)",
    "Split or broken tail fin",
    "Mismatched horns",
    "Transparent wing membranes", 
    "Bioluminescent markings",
    "Missing eye",
    "Clouded or milky eyes",
    "Feathers mixed with scales",
    "Gold-flecked scales",
    "Scales that change colour with mood",
    "Jagged crystal growths",
    "Naturally warm body",
    "Unnaturally cold body",
    "One oversized horn",
    "Venom dripping from fangs",
    "Burn marks across body",
    "Webbed claws",
    "Unusually long neck",
    "Crooked jaw",
    "Torn wings",
    "Wing membranes full of holes",
    "Glowing veins under scales",
    "Metallic scales",
    "Patchy scales from old illness",
    "Blind in one eye",
    "Forked tongue",
    "Double set of horns",
    "Antler-like horns",
    "Flowers or moss growing on body",
    "Fangs protrude even when mouth closed",
    "Extra wings",
    "Vestigial wings (too small to fly)",
    "Extremely long tail",
    "Stubby tail",
    "Oversized claws",
    "Retractable horns",
    "Naturally glowing blood",
    "Scales patterned like stars",
    "Pupil-less eyes",
    "Shadow seems to move on its own",
    "Echoing voice",
    "Mane instead of neck scales",
    "Whiskers like a sea dragon",
    "Four eyes",
    "Transparent scales in places",
    "Scars that glow with magic",
    "Scent of ozone or rainstorm",
    "Ears instead of horn frills",
    "Tail drags due to old injury",
    "Permanent limp",
    "Chains or jewelry fused into scales",
    "Voice crackles with magical interference",
    "Heterochromia (different coloured eyes)",
    "Extremely sharp teeth",
    "Glittering scales like gemstones",
    "Soft scales instead of hard plating",
    "Aura visible around body",
    "Long feathered tail",
    "Glowing tears",
]

# ----- DRAGON MOOD -----
moodoftheday = [
    "Aggressively affectionate",
    "Ready to fight the moon",
    "Sleepy but dangerous",
    "Emotionally attached to shiny objects",
    "Hissing at everyone for no reason",
    "Crying over something tiny",
    "Overconfident and underprepared",
    "Refusing to leave nest",
    "Causing problems on purpose",
    "Too much energy at 3am",
    "Deeply offended by existence",
    "Acts tough, secretly wants cuddles",
    "Hovering ominously in doorways",
    "One inconvenience away from arson",
    "Stealing snacks and denying it",
    "Wants attention but bites if given",
    "Trying to impress someone badly",
    "Existential crisis on rooftop",
    "Ferally protective of friends",
    "Dramatic sighing all day",
    "Obsessed with one random thing",
    "Will absolutely make things worse",
    "Purring like an engine",
    "Avoiding responsibilities creatively",
    "Dangerously curious",
    "Emotionally unstable but funny about it",
    "Tiny problem feels world-ending",
    "Ready to commit crimes for fun",
    "Making reckless financial decisions",
    "Hoarding random junk again",
    "Flirting with danger literally",
    "Can and will climb everything",
    "Unreasonably smug",
    "Needs a nap immediately",
    "Thinks rules are suggestions",
    "Picking fights with objects",
    "Emotionally attached to a stray creature",
    "Paranoid but accidentally correct",
    "Acting mysterious for attention",
    "Hyperfixated on a new hobby",
    "Accidentally intimidating civilians",
    "Running entirely on caffeine",
    "Staring into the void dramatically",
    "Wants to disappear into the woods",
    "Too soft for this world today",
    "Threatening violence over mild inconvenience",
    "Mischief levels critically high",
    "Nesting instinct activated",
    "Collecting trinkets like a crow",
    "Pretending not to care",
    "Being suspiciously nice",
    "Starting emotional conversations at terrible times",
    "Would lose a fight to stairs today",
    "Absolutely forbidden from touching magic artifacts",
    "In desperate need of enrichment",
    "Trying to look cool and failing",
    "Ready to overthrow authority",
    "Sulking beautifully",
    "Overstimulated and growling about it",
    "Making everyone else's problems their problem",
    "No thoughts, only vibes",
    "Mildly haunted",
    "Acting like an abandoned wet cat",
    "Chronically yearning",
    "Violently protective of their blanket pile",
    "One compliment away from emotional collapse",
    "Too prideful to ask for help",
    "Emotionally support dragon mode",
    "Would absolutely eat something they shouldn't",
    "Unstable but sparkly",
    "Trying very hard not to bite someone",
    "Ready to run away and join a circus",
    "Overly competitive about everything",
    "Possessed by goblin energy",
    "Feels like screaming into the ocean",
    "Convinced they are the smartest in the room",
    "Actually just wants to be held",
    "Low battery warning",
    "Feral but in a charming way",
    "Suspiciously calm",
    "Full cryptid mode",
    "Emotionally damaged and dramatic about it"
]
# ----- GANG EXCEP ITH -----
gang = ["Zevryn",  
    "Silk", 
    "Dr. Sevka", 
    "Ashara",
    "Nyx",
    "Ender",
    "Quin"
]

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

zevryn = [
    "cuddling with Ashara in her nest",
    "polishing and cleaning his weapons",
    "training in his training room",
    "going through a slow set of martial arts moves",
    "sitting cross-legged, his eyes closed, apparently meditating on something" 
    "discussing plans with the gang",
    "having a private chat with Silk",
    "out on a job to save some magical creatures",
    "trying to soothe a moody Ashara",
]

@bot.command()
async def theft(ctx):

    result = (
        f"{random.choice(thief)} stole "
        f"{random.choice(item)} from "
        f"{random.choice(victim)}. "
        f"When confronted, they {random.choice(react)}."
    )

    await ctx.send(result)

@bot.command()
async def prompt(ctx):

    result = (
        f"👥 {random.choice(charD)} and {random.choice(charL)}\n"
        f"⚔️ Conflict: {random.choice(prob)}\n"
        f"🎭 Vibes: {random.choice(mood)}\n"
        f"📦 Random inclusion: {random.choice(thing)}"
    )

    await ctx.send(result)

@bot.command()
async def dragon(ctx):

    result = (
        f"## Here there be dragons \n"
        f"**Species**: {random.choice(species)}\n"
        f"**Magic**: {random.choice(magic)}\n"
        f"**Colour**: {random.choice(colour)}\n"
        f"**Personality**: {random.choice(perso)}\n"
        f"**Trait**: {random.choice(trait)}\n"
    )

    await ctx.send(result)

@bot.command()
async def dragonmood(ctx):

    result = (
        f"-# Random dragon mood of the day \n"
        f"## {random.choice(moodoftheday)}\n"
    )

    await ctx.send(result)

@bot.command()
async def ith(ctx):

    result = (
        f"*Ithindril is currently {random.choice(ithindril)}*"
    )

    await ctx.send(result)

@bot.command()
async def ash(ctx):

    result = (
        f"*Ashara is currently {random.choice(ashara)}*"
    )

    await ctx.send(result)

@bot.command()
async def zev(ctx):

    result = (
        f"*Zevryn is currently {random.choice(zevryn)}*"
    )

    await ctx.send(result)

import os

bot.run(os.getenv("DISCORD_TOKEN"))
