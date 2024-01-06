
def counter(c):
    if c<=0:
        return c
    else:
        y = c+ counter(c-1)  #5+(5-1)    5+4+(4-1)  5+4+3+(3-1)  5+4+3+2+(2-1)  5+4+3+2+1
        print(y)
        return y
print(counter(5))


#____________factorial___________________________

def fact(n):
    if n ==1:
        print(n)
        return 1
    elif n==0:
        return 0
    else:
        x = n * fact(n-1)
        print(x)
        return x
print(fact(5))

#___________________________________________________________



def tri_recursion(k):
    if (k>0):
        result = k+tri_recursion(k-1)
        return result
    else:
        result = 0
        print(result)
    return result
print((tri_recursion(5)))