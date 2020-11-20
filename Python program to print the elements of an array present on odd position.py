#Python program to print the elements of an array present on odd position
#Initialize array     
arr = [9,10,11,12,13,14,15];     
print("Elements of given array present on odd position: ");    
#Loop through the array by incrementing the value of i by 2    
#Here, i will start from 1 as first even positioned element is present at position 1.    
for i in range(1, len(arr), 2):    
    print(arr[i]); 
