import math

class Series:
    def __init__(self, number):
        self.number = number

    def fib(self):
        res, count = 0, 0
        n1 = 0
        n2 = 1
        if self.number <= 0:
            print ("Must be a positive number")
        elif self.number == 1:
            print (n1)
        elif self.number == 2:
            print (n2)
        else:
            while count < self.number:
                res = n1 + n2
                print (n1)
                n1 = n2
                n2 = res
                count += 1
                
    def fact(self):
        if self.number < 0:
            print ("Must be a positive number!")
        else:
            count = 0
            n1 = self.number
            n2 = self.number - 1
            while count < self.number-1:
                ans = n1 * n2
                n2 -= 1
                n1 = ans
                count += 1
            print(ans)
            
    def prime(self):
        if self.number < 1:
            print ("Number must be greater than 0")
        else:
            i, j, flag = 0, 0, 0
            N = self.number
            for i in range(1, N+1, 1):
                if (i == 1 or i == 0): 
                    continue;
                #flag
                flag = 1
                
                for j in range(2, ((i // 2) + 1), 1): 
                    if (i % j == 0): 
                        flag = 0; 
                        break;
                
                if flag == 1:
                    print (i, end = " ")
                    

def harmonic(n):
        if n < 2:
            return 1
        else:
            return 1 / n + (harmonic(n - 1))
  
  
  
def geo(a, r, n) : 
    
    sum = 0
    i = 0
    while i < n : 
        sum = sum + a 
        a = a * r 
        i = i + 1
    
    return sum
    

num = Series(5)
num.prime()
harmonic(4)