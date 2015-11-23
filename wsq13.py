from math import *

def rooty():
    og = float(input("Square root of which number you want to know? "))
    guess = 1
    while True:
        last = guess
        guess = (1/2)*(guess + (og/guess))
        if (guess == last):
            return(guess)
            break


print("The square root is: ", rooty())
