#a = 5
#b = 7

a = input("First number: ")
b = input("Second number: ")


try:
    val1 = int(a)
    val2 = int(b)
    if a > b:
        print (str(a) + " is bigger")
    else:
        print (str(b) + " is bigger")
except ValueError:
    print("Input integer values!!!")




