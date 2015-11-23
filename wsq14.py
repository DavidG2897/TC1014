def calculate_e(precision):
    e = 2
    for i in range(1,precision+1):
        e = (1 + 1/i)**i
    e = str(e)
    return(e[:precision + 2])

print(calculate_e(4))
