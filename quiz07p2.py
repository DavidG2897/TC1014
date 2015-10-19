def fibonacci(n):
    x = 0
    m = 1
    if (n < 1):
        return (0)
    else:
        for i in range(n):
            num = x + m
            m = x
            x = num
        return(num)

print(fibonacci(8))
