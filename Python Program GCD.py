#Greatest Common Devisior Of Two Numbers

n1=int(input('enter the first number:'))
n2=int(input('enter the second number:'))
if n1>n2:
   smallest=n1
else:
   smallest=n2
for i in range(1,smallest+1):
   if n1%i==0 and n2%i==0:
      gcd=i
print('gcd is:',gcd)

# Using Functions

def gcd(n1, n2):
   if n1 > n2:
      small = n2
   else:
      small = n1
      for i in range(1, small+1):
         if((n1 % i == 0) and (n2 % i == 0)):
            gcd = i
      return gcd 

a = int(input('enter number'))
b= int(input('enter number'))

print ('The gcd of',a,'and', b, 'is', ':' ,"end=") 
print (gcd(a,b))

#Using Math Module
import math

a = int(input('enter number'))
b= int(input('enter number'))
c=math.gcd(a,b) #dir(math)--->gcd
print('Gcd of',a,'and',b,'is',c)

