import random
import re
import time

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
    "what is your name?": [
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
        'you tell me!'
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

rules = {
    'I want (.*)': [
        'What would it mean if you got {0}',
        'Why do you want {0}',
        "What's stopping you from getting {0}"
    ],
    'do you remember (.*)': [
        'Did you think I would forget {0}',
        "Why haven't you been able to forget {0}",
        'What about {0}',
        'Yes .. and?'
    ],
    'do you think (.*)': [
        'if {0}? Absolutely.',
        'No chance'
    ],
    'if (.*)': [
        "Do you really think it's likely that {0}",
        'Do you wish that {0}',
        'What do you think about {0}',
        'Really--if {0}'
    ]
}


# Define match_rule()
def match_rule(rule, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rule.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase


# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me', 'you', message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my', 'your', message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your', 'my', message)
    if 'you' in message:
        # Replace 'you' with 'i'
        return re.sub('you', 'i', message)

    return message


# Define respond()
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        response = random.choice(responses[message])
        return response
    # Check for a question mark
    elif message.endswith('?'):
        # Return a random question
        response = random.choice(responses["question"])
        return response
    else:
        # Call match_rule
        response, phrase = match_rule(rules, message)
        if '{0}' in response:
            # Replace the pronouns in the phrase
            phrase = replace_pronouns(phrase)
            # Include the phrase in the response
            response = response.format(phrase)
            return response
        else:
            # Return a random statement
            response = random.choice(responses["statement"])
            return response


def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    time.sleep(2)
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    time.sleep(2)


# Send the messages
send_message(input("Ask Me: ").lower())
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
send_message("what's your name?")
send_message("what's my name?")
send_message("how are you?")
send_message("I love building chatbots")
send_message("I love building chatbots")
