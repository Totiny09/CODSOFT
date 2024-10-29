import random


def random_string():

    random_response_list = ["Please try writing something more descriptive.",
                            "Oh! It appears you wrote something I don't understand yet",
                            "Do you mind trying to rephrase that?",
                            "I'm terribly sorry, I didn't quite catch that.",
                            "I can't answer that yet, please try asking something else."
                            ]

    response = random_response_list[random.randint(0, len(random_response_list))]

    return response

print(random_string())