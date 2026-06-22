import random


silk = [
    "negotiating a deal",
    "bothering Nyx for fun",
    "flirting with someone for information",
    "working a room full of potential contacts",
    "making a suspicious number of phone calls",
    "collecting rumors from across the city",
    "convincing someone to do him a favor",
    "planning his next business venture",
    "reviewing a list of potential clients",
    "trying to talk his way out of trouble",
    "charming information out of a reluctant source",
    "enjoying an expensive cup of coffee",
    "lounging in a chair like he owns the place",
    "watching the chaos unfold with amusement",
    "making connections that somehow benefit everyone",
    "tracking down a hard-to-find contact",
    "sending messages to his network",
    "meeting with one of his informants",
    "negotiating better terms on a contract",
    "casually gathering information from unsuspecting people",
    "checking in on one of the gang members",
    "bringing snacks back for everyone",
    "having a private chat with Zevryn",
    "giving Ender questionable advice",
    "listening to Dr. Sevka explain something complicated",
    "trying to convince Ashara to help with a scheme",
    "helping Nyx despite claiming otherwise",
    "making sure everyone has what they need",
    "covering for one of the gang members",
    "organizing an outing for the group",
    "starting a rumor just to see what happens",
    "planning something that definitely isn't a prank",
    "being banned from somewhere again",
    "talking his way into a place he shouldn't be",
    "seeing how many people he can annoy before lunch",
    "causing minor problems for his own entertainment",
    "teasing Zevryn mercilessly",
    "attempting to recruit Nyx into a bad idea",
    "looking far too pleased with himself",
    "refusing to explain what he's smiling about",
    "quietly helping someone who needed it",
    "reading through old messages from friends",
    "checking on a rescued creature",
    "sitting somewhere peaceful for once",
    "watching over the warehouse while everyone sleeps",
    "donating anonymously to a good cause",
    "making sure nobody notices he's worried",
    "thinking about people he misses",
    "taking a rare moment to himself",
    "pretending he doesn't care when he absolutely does",
    "trying to look innocent",
    "absolutely not causing trouble",
    "being blamed for something he may or may not have done",
    "talking his way into free food",
    "wondering how he became the responsible one",
    "hiding from the consequences of his actions",
    "avoiding several people looking for him",
    "working on a plan that somehow involves three favors and a pigeon",
    "claiming everything is under control",
    "making promises that are technically not lies"
]

def setup(bot):
    @bot.command()
    async def silk(ctx):

        result = (
            f"*Silk is currently {random.choice(silk)}*"
        )

        await ctx.send(result)
