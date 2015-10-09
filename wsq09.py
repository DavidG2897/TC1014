def work():
    while True:
        try:
            n = int(input("Enter a non-negative integer:"))
            if (n <= 0):
                print("Non-negative and different from 0 please.")
            else:
                break
        except ValueError:
            print("Integer!")

    factorial = 1
    for x in range(n):
        factorial = factorial * n
        n = n - 1
    print ("Factorial:", factorial)

work()

while True:
    y = input("Would you like to try another number? ")
    if(y == "yes"):
        y = input("Are you sure? ")
        if (y == "yes"):
            work()
        elif (y == "no"):
            print ("Ok! Have a nice day.")
            break
    elif (y == "no"):
        print ("Ok! Have a nice day.")
        break
