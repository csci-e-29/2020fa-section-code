import random


def greet(person_name):
    responses = [
        'Howdy',
        "Hey there",
        "Nice to meet you",
        "Fine weather we're having",
        "Salutations",
        "Heckuva day",
        "Top of the morning to ya",
        "Greetings"
    ]
    return f"{responses[random.randrange(len(responses))]}, {person_name}"
