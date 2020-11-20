#Python program to print the largest element in an array
#Initialize array     
arr = [10,25,12,17,79,53];     
#Initialize max variable with first element of array.    
max = arr[0];    
#Loop through the array    
for i in range(0, len(arr)):    
#Compare elements of array with max variable and find greater than max then ovveride max variable with new value  
   if(arr[i] > max):    
       max = arr[i];    
print("Largest element in given array = " + str(max));
