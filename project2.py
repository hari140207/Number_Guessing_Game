import random

secret_number =  random.randint(1,10)



print("Welcome to Guessing number Game!")
print("Guess a number betweeen 1 and 10")


guess =  int(input("enter your guess:"))
print("----------------------------------")


if guess  == secret_number:
    print("You Guessed Correct number!!!")
else :
    print("Wrong Guess!")
    print("Try Again!")