#Can you guess the number?
import random
random_number = random.randint(1, 50)
print("I'm thinking of a number between 1 and 50.")

#Ask the player to guess 8 times.
for guesses in range (1, 9):
    print("Take a guess.")
    guess = int(input())

    if guess < random_number:
        print("Too low.")
    elif guess > random_number:
        print("Too high.")
    else:
        break #this is the correct answer

if guess == random_number:
    print("Good job. You guessed correctly in " + str(guesses) + " guesses.")
else:
    print("Too bad. The number was " + str(random_number) + ".")