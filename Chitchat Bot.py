import time
import random

user_template = "USER : {0}"
bot_template = "BOT : {0}\n"

# Define variables
name = "Chitty"
weather = "Cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
    "what's your name?": [
        "my name is {0}".format(name),
        "they call me {0}".format(name),
        "I go by {0}".format(name)
    ],
    "what's today's weather?": [
        "the weather is {0}".format(weather),
        "it's {0} today".format(weather)
    ],
    "question": [
        "I don't know :(",
        'you tell me!',
        "Sadly i don't know"
    ],
    "statement": [
        'tell me more!',
        'why do you think that?',
        'how long have you felt this way?',
        'I find that extremely interesting',
        'can you back that up?',
        'oh wow!',
        ':)'
    ],
    "default": ["default message"]
}


# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
        return bot_message
    # Check for a question mark
    elif message.endswith('?'):
        # Return a random question
        bot_message = random.choice(responses["question"])
        return bot_message
    else:
        # Return a random statement
        bot_message = random.choice(responses["statement"])
        return bot_message


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    time.sleep(1)
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))


send_message("what's your name?")

send_message("what's my name?")
send_message("how are you?")

send_message("I love building chatbots")
send_message("I love building chatbots")
