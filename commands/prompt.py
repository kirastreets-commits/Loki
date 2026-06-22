import random

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

location = [
    "the warehouse",
    "Ashara's nest",
    "a rescue mission",
    "the city",
    "a forest",
    "a marketplace",
    "a rooftop",
    "Ender's room",
    "Sevka's Lab",
    "a special event",
    "the industrial disctrict"
]

def setup(bot):
    @bot.command()
    async def prompt(ctx):

        result = (
            f"## {random.choice(charD)} and {random.choice(charL)}\n"
            f"📍 Location: **{random.choice(location)}**\n"
            f"⚔️ **{random.choice(prob)}**\n"
            f"🎭 Vibes: **{random.choice(mood)}**\n"
            f"📦 Random inclusion: **{random.choice(thing)}**"
        )

        await ctx.send(result)
