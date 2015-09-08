print("Im asking for the first and the last numbers of a range.")

while True:
    try:
        x = int(input("Please give me the first number:"))
        y = int(input("Please give me the last number:"))
        if(x > y):
            print(x,"is greater than",y,"! Please give me the right order.")
        elif(x == y):
            print("Please, give me different values.")
        else:
            suma = 0
            for n in range(x,y+1):
                suma = suma + n
            print ("The sum from",x,"to",y,"is:",suma)
            break
    except ValueError:
        print("Don't you dare! (Please enter an integer).")
