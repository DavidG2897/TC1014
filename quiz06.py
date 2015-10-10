def superpower(x,y):
    n = 1
    for i in range(y):
        n = n * x
    return(n)

def stars(s):
    star = ""
    for i in range(s):
        star = star + "*"
    print(star)

print(superpower(3,4))
stars(5)
