import random

print("Number Guessing Game")
number=random.randint(1,9)
chances=0

while chances<5:
    guess=int(input("Enter a Number 1-9"))
    if guess==number:
        print("You guessed correctly")
    elif guess<number:
        print("You guesses too low") 
    else:
        print("You guessed too high")
    chances+=1

if not chances<5:
    print("You lose and the number is",number)