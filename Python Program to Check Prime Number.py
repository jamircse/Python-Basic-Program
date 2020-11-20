n=int(input('Enter the number to check prime : '));
count=0;
i=2;
while(i<n):
    if(n%i==0):
        count=count+1;
        break;
    i+=1;
if(count==0):
    print(n,' is a prime number');
else:
    print(n,'is not a prime number ');
