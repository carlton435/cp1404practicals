"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random
number = float(input("Enter the number of score: "))
time = 0
while time < number:
    score = random.randint(1,100)
    time = time + 1
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("{} is Invalid score".format(score))
        if 50 < score <90:
            print("{} is Passable".format(score))
        if 90 < score <=100 :
            print("{} is Excellent".format(score))

    if score < 50:
        print("{} is Bad".format(score))
