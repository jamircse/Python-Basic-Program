#prime number generation
sum=0
starting=int(input('enter the starting number: '))
ending=int(input('enter the ending number: '))
print("Prime numbers between",starting,"and",ending,"are:")
for i in range(starting,ending+1):
   if starting>1:
      for j in range(2,i):
         if i %j==0:
            break
      else:
         sum=sum+i
         print(i,end=' ,')
print('\nsum is',sum)
      


