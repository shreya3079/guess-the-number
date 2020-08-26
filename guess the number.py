import random

process = True
no = random.randint(0, 100)
chance = 0
print("Enter a number between 0 to 100\n")
print("You have only 5 chances to guess the number\n")

while process:
    choice = input("Guess the number:")
    if int(choice) == no:
        print("Yeah!!! You guessed the number!!!")
        print("Would you like to play it again?", "\n 1. Yes \n 2. No")
        option = input()
        if option == str(1):
            chance = 0
            pass
        if option == str(2):
            exit("Thanks for playing!!! See you again")
    elif int(choice) > no:
        print("Number is too high")
        chance = chance + 1

    elif int(choice) < no:
        print("Number is too low")
        chance = chance + 1
    else:
        continue

    if int(chance) == 5:
        print("You have reached the limit")
        print("The number was ", no)
        exit()