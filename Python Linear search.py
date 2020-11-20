n=int(input('enter the required no of values:'))
l1=[]
for i in range(0,n):
   p=int(input('enter the numbers:'))
   l1.append(p)
s=int(input('enter the required search value:'))
j=count=0
while j<len(l1):
   if l1[j]==s:
      count=1
      break
   j=j+1
if count==1:
      print('value found at:',j,'address')
else:
      print('value is not found')
         
