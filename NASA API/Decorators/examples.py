def shout(text):
    return text.upper() + '!'

def whisper(text, delay=0.05):
    return text.lower() + '.'

def greet(func):
    greeting = func("Hello!")
    print(greeting)


print("I'm shouting:", shout('hello'))
yell = shout

print(yell("Elon Musk"))

greet(shout)


