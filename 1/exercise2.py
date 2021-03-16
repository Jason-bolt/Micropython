#a = 5
#b = 3

#print (a+b)
#print (a-b)
#print (a*b)
#print (a/b)

#getting the user values
calculate = input("Operation: ")
#splitting the string according to spaces
calcarray = calculate.split()
#assigning values to variables
num1 = float(calcarray[0])
operation = calcarray[1]
num2 = float(calcarray[2])

if operation == '+':
    print (num1 + num2)
elif operation == '-':
    print (num1 - num2)
elif operation == '/':
    print (num1 / num2)
elif operation == '*':
    print (num1 * num2)
