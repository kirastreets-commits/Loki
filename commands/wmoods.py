import random

ZEVRYN_MOODS = [
    "Focused", "Focused", "Focused",
    "Calm", "Calm", "Calm",
    "Determined", "Determined",
    "Protective", "Protective",
    "Reflective",
    "Tired",
    "Concerned",
    "Frustrated",
    "Hopeful",
    "Mission-Oriented", "Protective",
    "Brooding"
]

QUIN_MOODS = [
    "Happy", "Happy", "Happy",
    "Excited", "Excited", "Excited",
    "Playful", "Playful", "Playful",
    "Affectionate", "Affectionate",
    "Curious", "Curious",
    "Energetic", "Energetic",
    "Inspired",
    "Distracted",
    "Tired",
    "Songful", "Nest-Brained", "Brooding"
]

ENDER_MOODS = [
    "Focused", "Focused", "Focused",
    "Curious", "Curious", "Curious",
    "Content", "Content",
    "Calm", "Calm",
    "Amused", "Amused",
    "Inspired", "Inspired",
    "Happy",
    "Affectionate",
    "Tired", "Tired",
    "Distracted",
    "Overwhelmed",
    "Concerned",
    "Determined",
    "Hopeful",
    "Hyperfocused"
    "Debugging",
    "Inventive",
    "Problem-Solving",
    "Technically Concerned",
    "Running on Coffee"
]

SILK_MOODS = [
    "Content", "Content",
    "Confident", "Confident", "Confident",
    "Playful", "Playful",
    "Amused", "Amused",
    "Curious",
    "Focused",
    "Affectionate",
    "Restless",
    "Frustrated",
    "Mischievous", "Mischievous", "Mischievous",
    "Scheming", "Smug"
]

NYX_MOODS = [
    "Calm", "Calm",
    "Focused", "Focused",
    "Neutral", "Neutral",
    "Reflective", "Reflective",
    "Tired",
    "Protective",
    "Sensitive",
    "Conflicted",
    "Anxious",
    "Determined",
    "Brooding", "Observant"
]

SEVKA_MOODS = [
    "Focused", "Focused", "Focused",
    "Calm", "Calm",
    "Tired", "Tired",
    "Concerned", "Concerned",
    "Curious", "Curious",
    "Hopeful",
    "Overwhelmed",
    "Reflective",
    "Content",
    "Scientifically Concerned"
]

ASHARA_MOODS = [
    "Happy", "Happy", "Happy",
    "Playful", "Playful", "Playful",
    "Affectionate", "Affectionate", "Affectionate",
    "Energetic", "Energetic",
    "Excited", "Excited",
    "Content",
    "Restless",
    "Frustrated",
    "Agitated",
    "Playful-chaotic", "Playful-chaotic", "Playful-chaotic",
    "Hangry", "Attention-Seeking", "Cuddle-Deprived", "Brooding"
]

ITHINDRIL_MOODS = [
    "Playful", "Playful", "Playful",
    "Curious", "Curious", "Curious",
    "Excited", "Excited",
    "Energetic", "Energetic",
    "Affectionate",
    "Happy", "Happy",
    "Playful-chaotic", "Playful-chaotic", "Playful-chaotic",
    "Distracted",
    "Restless",
    "Mischievous", "Mischievous",
    "Gremlin Mode", "Treasure-Hunting"
]

def setup(bot):

    @bot.command()
    async def wmoods(ctx):

        result = (
            "📋 **Current Warehouse Moods**\n\n"
            f"⚔️ Zevryn: {random.choice(ZEVRYN_MOODS)}\n"
            f"🐦 Quin: {random.choice(QUIN_MOODS)}\n"
            f"🛠️ Ender: {random.choice(ENDER_MOODS)}\n"
            f"🦊 Silk: {random.choice(SILK_MOODS)}\n"
            f"🌙 Nyx: {random.choice(NYX_MOODS)}\n"
            f"🧪 Dr. Sevka: {random.choice(SEVKA_MOODS)}\n"
            f"🐉 Ashara: {random.choice(ASHARA_MOODS)}\n"
            f"🐲 Ithindril: {random.choice(ITHINDRIL_MOODS)}"
        )

        await ctx.send(result)
