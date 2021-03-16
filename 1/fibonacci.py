def Fib(n):
    res, count = 0, 0
    n1 = 0
    n2 = 1
    if n <= 0:
        print ("Must be a positive number")
    elif n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        while count < n:
            res = n1 + n2
            print (n1)
            n1 = n2
            n2 = res
            count += 1
    
print (Fib(10))