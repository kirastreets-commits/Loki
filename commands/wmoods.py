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
    "Hopeful"
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
    "Tired"
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
    "Mischievous", "Mischievous", "Mischievous"
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
    "Determined"
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
    "Content"
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
    "Playful-chaotic", "Playful-chaotic", "Playful-chaotic"
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
    "Mischievous", "Mischievous"
]

def setup(bot):

    @bot.command()
    async def wmoods(ctx):

        result = (
            "📋 **Current Warehouse Moods**\n\n"
            f"⚔️ Zevryn: {random.choice(ZEVRYN_MOODS)}\n"
            f"🐦 Quin: {random.choice(QUIN_MOODS)}\n"
            f"🦊 Silk: {random.choice(SILK_MOODS)}\n"
            f"🌙 Nyx: {random.choice(NYX_MOODS)}\n"
            f"🧪 Dr. Sevka: {random.choice(SEVKA_MOODS)}\n"
            f"🐉 Ashara: {random.choice(ASHARA_MOODS)}\n"
            f"🐲 Ithindril: {random.choice(ITHINDRIL_MOODS)}"
        )

        await ctx.send(result)
