
def recursion(n):
   if n <= 1:
       return n
   else:
       return(recursion(n-1) + recursion(n-2))
nterms = int(input("How many terms? "))
print("Fibonacci sequence:")
for i in range(nterms):
    print(recursion(i))










def fibonacci(n):
    if n<=1:
        return n
    else:
        x=fibonacci(n-1)
        print("x value",x)
        z=fibonacci(n-2)
        print("z",z)
        y= fibonacci(n-1)+fibonacci(n-2)
        print(y)
        return y

print(fibonacci(5))


