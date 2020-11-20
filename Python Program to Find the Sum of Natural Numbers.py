num = int(input("Enter a number: "))
num2=num
if num < 0:  
  print("Enter a positive number")  
else:  
  sum = 0  
# use while loop to iterate un till zero  
while(num > 0):  
   sum += num  
   num -= 1  
print("The sum is",sum) 

# use for loop to iterate
sum=0
for i in range(0,num2+1):
    sum=sum+i
print("The sum is",sum)


