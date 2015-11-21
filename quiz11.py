from math import *

def calculateE(accuracy):
    n = 1
    i = 0
    last = 0
    while True:
        e = 1/factorial(i)
        i = i + 1
        last = last + e
        if(n <= (last + accuracy) and n >= (last - accuracy) and n != 1):
            return(last)
            break
        n = last

def checkBanana(banana):
    n = 0
    fil = open(banana)
    read = fil.read()
    words = read.split()
    for i in words:
        i = i.lower()
        if (i == "banana"):
            n = n + 1
    print("banana appears",n,"times")

print(calculateE(0))
checkBanana("banana.txt")
