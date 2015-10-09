while True:
    try:
        x = int(input("Input first integer: "))
        y = int(input("Input second integer: "))
        break
    except ValueError:
        print ("Don't you dare!")

def suma(x,y):
    a = x + y
    return (a)

def difference(x,y):
    a = x - y
    return (a)

def product(x,y):
    a = x * y
    return (a)

def int_division(x,y):
    a = x // y
    return (a)

def remainder(x,y):
    a = x % y
    return (a)

print ("The sum is", suma(x,y))
print ("The difference is", difference(x,y))
print ("The product is", product(x,y))
print ("The integer division", int_division(x,y))
print ("The raminder is", remainder(x,y))
