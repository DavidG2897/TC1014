from math import *

def distance(x1,y1,x2,y2):
    d = sqrt((x2 - x1)**2+(y2 - y1)**2)
    return(d)

print(distance(2,3,5,6))
