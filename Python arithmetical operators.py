# Python arithmatic operators are + - / * %  plus minus multiply devided Remainder

def add(x,y):
    return x+y   # +
def sub(x,y):
    return x-y
def mul(x,y):
    result=x*y
    return result
def div(x,y):
    result =float(x/y)
    return result
def remainder(x,y):
    result=int(x%y)
    return result


num1=int(input("Enter the first number : "))
num2=int(input("Enter the Second number : "))

print('add = ',add(num1,num2))

print('substraction  = ',sub(num1,num2))

print('Multiplication = ',mul(num1,num2))

print('divition = ',div(num1,num2))

print('remainder = ',remainder(num1,num2))

