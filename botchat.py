import random

responses = {
    "hi": ["Hello", "Hi there", "Hi"],
    "how are you": ["I'm doing well, thank you!", "I'm doing pretty good", "I'm fine, thank you"],
    "what are you doing": ["Just chatting with you", "Nothing much", "Just hanging out"],
    "bye": ["Goodbye", "Bye!", "See you later"],
    "whats your name": ["my name is Ronin 2.0", "ronin 2.0: the new age bot", "hail donan,im ronin"],
    "whats your age": ["I'm 2 days old"],
    "adipoli": ["maple yenna panringa...?"],
    "macha": ["helu macha"],
    "long drive polama": ["pollam macha, ana petrol needa oothunu....en kitta kas illa da :`-( "],
    "tell me a joke": ["One joke, coming up! What is a sea monster’s favorite snack? Ships and dip. 🛳",
                       "One joke, This might make you laugh. How do robots eat guacamole? With computer chips",
                        "One joke, What did one snowman say to the other?Do you smell carrots?" ]
}

def bot1():
    while True:
        message = input("Bot 1: ")
        if message.lower() in responses:
            print(random.choice(responses[message.lower()]))
        else:
            print("I don't understand what you're saying.")

def bot2():
    while True:
        message = input("Bot 2: ")
        if message.lower() in responses:
            print(random.choice(responses[message.lower()]))
        else:
            print("I don't understand what you're saying.")
            
bot1()
bot2()
