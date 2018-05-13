#!/usr/bin/python3.6
# -*-coding: UTF-8-*-
import random

secret = random.randint(1, 100)
guess = 0
tries = 0

print("AHOY! I'm the Dead Pirate Robots,and I have a very mischevious secret!")
print("It is a number from 1 to 99. I shall give you 6 tries!")

while guess != secret and tries < 6:
    guess = int(input("Well, What's yer guess? "))
    if guess < secret:
        print("Too low, ye scurvy dog !")
    elif guess > secret:
        print("Too high, landblubber!")
    tries = tries + 1
if guess == secret:
    print("Avast! Ye got it! Found my secret, ye did!")
else:
    print("No more guesses! Better luck next time, matey!")
    print("The secrect number was", secret)
