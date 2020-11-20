
name=str(input("Enter the string to check reverse : ")); 
length=len(name)  
n=0  
for i in range(-1,(-length-1),-1):  
    print(name[n],"\t",name[i]) 
    n+=1 ;
