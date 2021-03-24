import re

chat = []

chat.append(["h(i|ello)", "Hi", [], []])
chat.append(["I like .", "Me too", [], []])
chat.append(["oh my g(o|aw)d ?!*", "What is the meaning of life?", [], []])
chat.append(["(who|what)(\'?s| is) your wife(\'?s name)?\??", "Siri", [], []])

while True:
    text = input("You: ")

    for section in chat:
        current = section[0]
        if re.search(current, text, flags=re.I):
            out = section[1]
            break
        else:
            out = "I do not understand"

    print("Bot: " + out)