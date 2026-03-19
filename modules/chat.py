import random
intents = [
    {
        "tag" : "greeting",
        "patterns" : ["hello" , "hi" , "hey"],
        "responce" : ["Hi, How can i help...", "Hii, how's life going?" , "Heyyy, how are you?"]
    },
    {
        "tag" : "status",
        "patterns" : ["how are you","how r u", "what about you" , "how bout you" , "how bout u"],
        "responce" : ["I'm fine how about you?" , "I'm perfectly fine, how about you sir?"]
    }
]
def reply(command):
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern in command:
                return random.choice(intent["responce"])
    return None
