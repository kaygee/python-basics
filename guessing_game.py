import random

random_number = random.randint(1, 10)
chances_amount = 3
guessed_amount = 0

def prompt_for_input():
    print("I've chosen a number between 1 and 10!")
    print("You've guessed {} times and have {} guesses left.".format(guessed_amount, chances_amount))

while chances_amount > 0:
    prompt_for_input()

    try:
        user_guess = int(input("> "))
    except:
        print("Oops! That wasn't a whole number!")
        break

    chances_amount -= 1
    guessed_amount += 1

    if user_guess == random_number:
        print("Yup! I chose {}!".format(random_number))
        print("It took you {} tries!".format(guessed_amount))
        break
    elif user_guess < random_number:
        print("You guessed too low!")
        continue
    elif user_guess > random_number:
        print("You guessed too high!")
        continue
        
