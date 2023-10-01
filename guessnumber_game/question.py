import sys
import random


max = input("What is the maximum number?")
min = input("What is the minimum number?")
answer = random.randint(int(min), int(max)) 
for i in range(10):
    guess = input("Guess the number")
    if int(guess) == answer:
        print("You did it")
        break
    else:
        print("You failed")
    if i == 9:
        print("Game Over!")