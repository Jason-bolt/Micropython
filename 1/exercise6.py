class Series:
    def __init__(self):
        self.name = "Jason"

    def fib(self, number):
        res, count = 0, 0
        fib = []
        n1 = 0
        n2 = 1
        if number <= 0:
            caution = "Must be a positive number"
            return caution
        elif number == 1:
            return 0
        elif number == 2:
            return 1
        else:
            while count < number:
                res = n1 + n2
                fib.append(n1)
                n1 = n2
                n2 = res
                count += 1
            for a in fib:
                print (a)
                
    def fact(self, number):
        if number < 0:
            print ("Must be a positive number!")
        elif number == 1:
            return 1
        else:
            return self.fact(number - 1) * number
            
    def prime(self, number):
        if number < 1:
            print ("Number must be greater than 0")
        else:
            i, j, flag = 0, 0, 0
            N = number
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
                    
    def geometric(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return 1
        else:
            return self.geometric(number-1) + (1/(2**number))
                    

    def harmonic(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return 1
        else:
            return self.geometric(number-1) + (1/number)
      
    def unknownSeries1(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return (((-1)**(number + 1))/number)
        else:
            return self.unknownSeries1(number - 1) + (((-1)**(number + 1))/number)
        
    def unknownSeries2(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return (((-1)**(number+1))*(4)/((2*number)-1))
        else:
            return self.unknownSeries2(number - 1) + (((-1)**(number+1))*(4)/((2*number)-1))
        
    def unknownSeries3(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return 2
        else:
            return self.unknownSeries3(number - 1) * (((2*(number -1)) * (2*(number -1)))/((number - 1) * (number + 1)))
        
    def unknownSeries4(self, number):
        if number < 1:
            caution = "Number must be greater or equal to 1"
            return caution
        elif number == 1:
            return ((-1)**number)/(self.fact(number))
        else:
            return self.unknownSeries4(number - 1) + ((-1)**number)/(self.fact(number))


num = Series()
print(num.unknownSeries3(2))