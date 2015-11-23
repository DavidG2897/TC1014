def gcd(a,b):
    if (a == b):
        return (a)
    else:
        if(a > b):
            return (gcd(a-b,b))
        else:
            return (gcd(a,b-a))

a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("The GCD is",gcd(a,b))
