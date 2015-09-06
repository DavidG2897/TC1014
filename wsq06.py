from random import *
x = randint(1,100)
y = 0
n = 0       #Try counter
print ("I chose an integer between 1 and 100.")

def guess(y,x,n):
        while y != x:
            try:    #while loop that check if y is different from x
                y = int(input("Guess the integer: "))
                if (y < x):
                    print ("Too low! Try again.")
                    n = n + 1
                elif (y > x):
                    print ("Too high! Try again.")
                    n = n + 1
                else:
                    print ("You guessed it right!")
                    n = n + 1
                    print ("You tried",n,"times.")
            except ValueError:
                print("That's not an integer!")
guess(y,x,n)
