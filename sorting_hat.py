import random

houses = ["griffindor", "huffilpuff", "slythryn", "ravinclaw"]

name = raw_input("What's yo name bitch? ")
print("What house u want bitch?\nYour options are:"),
for x in range(len(houses)):
    print(houses[x]),
print
preference = raw_input()
print('Sorry %s, you ain\'t getting that house bitch' % name)
houses.remove(str.lower(preference))
random_number = random.randint(0, len(houses) - 1)
energy = raw_input("Are you a top or bottom bitch? ")
houses.remove(houses[random.randint(0, len(houses) - 1)])
print("Oh! So you think you're a %s bitch?" %energy)
ass_or_titties = raw_input("Ass or titties bitch? ")
houses. remove(houses[random.randint(0, len(houses) - 1)])
print("I knew you were a %s person btich. " % ass_or_titties)
print("You in " + houses[0].capitalize() + " bitch")
