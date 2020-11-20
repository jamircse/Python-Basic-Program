#Python program to print the elements of an array in reverse order
#Initialize array  with 5 values corresponding 10 20 30 40 50   
array = [10,20,30,40,50];     
print("Here is the Original array: ");    
for i in range(0, len(array)):    
    print(array[i]),     
print("Here is Array in reverse order: ");    
#Loop through the array in reverse order    
for i in range(len(array)-1, -1, -1):     
    print(array[i]),  


