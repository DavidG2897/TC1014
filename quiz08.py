def dot_product(v1,v2):
    if(len(v1) != len(v2)):
        o = float("NaN")
        return(o)
    else:
        val = 0
        for i in range(0,len(v1)):
            p = v1[i] * v2[i]
            val = val + p
        return(val)

print(dot_product([2,4,5,6],[1,2,3,4]))
