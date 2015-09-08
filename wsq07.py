print("Im asking for the first and the last numbers of a range.")

def validate():
    while True:
        try:
            x = int(input("Please give me the first number:"))
            y = int(input("Please give me the last number:"))
            if(x > y):
                print(x,"is greater than",y,"! Please give me the right order.")
            elif(x == y):
                print("Please, give me different values.")
            else:
                print("The sum from",x,"to",y,"is",sum(range(x,y+1)))
                break
        except ValueError:
            print("Don't you dare! (Please enter an integer).")

validate()
