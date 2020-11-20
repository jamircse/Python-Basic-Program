#Python program to print all pronic numbers between 1 and 100
#Like 2(2+1) = 6 can be called as a pronic number.
#isPronicNumber() will determine whether a given number is a pronic number or not    
def isPronicNumber(num):    
    flag = False;    
    for j in range(1, num+1):    
    #Checks for pronic number by multiplying consecutive numbers    
         if((j*(j+1)) == num):    
              flag = True;    
              break  
    return flag   
#Displays pronic numbers between 1 and 100    
print("Pronic numbers between 1 and 100: ");    
for i in range(1, 101):    
    if(isPronicNumber(i)):    
        print(i),    
        print(" "),     
