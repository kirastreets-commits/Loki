import random

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