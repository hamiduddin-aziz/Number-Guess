
# project 2 number guess game

import random

max_range = input("Pick a number for the top range that is greater than 0: ")

if max_range.isdigit() and int(max_range) > 0:
    max_range = int(max_range)
else:
    print("The input must be a digit that is larger than 0.")
    quit()
ran = random.randint(0, max_range)
print("Now try to guess the number that will be generated randomly.")
while True:
    answer = input("Your guess? ")
    if int(answer) == ran:
        print("Congratulations, you got it!")
        break
    elif int(answer)>ran:
        print("You got it wrong. your answer were above the number. Try again.")
    else:
        print("You got it wrong. your answer were below the number. Try again.")
