#Python program to print the smallest element in an array
#Initialize array     
arr = [25, 21, 7, 37, 56, 32, 84, 13, 9, 18];      
#Initialize min with the first element of the array.    
min = arr[0];    
#Loop through the array    
for i in range(0, len(arr)):    
#Compare elements of array with min    
    if(arr[i] < min):    
       min = arr[i];    
print("Smallest element present in given array: " + str(min));  
