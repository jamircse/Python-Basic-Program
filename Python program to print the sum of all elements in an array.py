#Python program to print the sum of all elements in an array
#Initialize array     
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];     
sum = 0;    
#Loop through the array to calculate sum of elements    
for i in range(0, len(arr)):    
     sum = sum + arr[i];    
print("Sum of all the elements of an array: " + str(sum));  
