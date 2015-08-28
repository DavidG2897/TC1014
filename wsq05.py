x = input("Temperature in degrees Fahrenheit: ")
x = int(x)
y = 5 * (x - 32)/9  # y are degrees Celsius
y = round(y)

print (x,"degrees Fahrenheit are",y,"degrees Celsius.")

if(y >= 100):
    print("Water boils at this temperature.")
else:
    print("Water does not boil at this teperature")
