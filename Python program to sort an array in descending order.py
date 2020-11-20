#Python program to sort an array in descending order
#Initialize array     
arr = [5, 2, 8, 7, 1, 3, 13, 64, 23, 15, 48, 39, 9];     
temp = 0;    
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):    
     print(arr[i], end=" ");    
#Sort the array in descending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
          if(arr[i] < arr[j]):    
              temp = arr[i];    
              arr[i] = arr[j];    
              arr[j] = temp;    
print('\n\n')    
#Displaying elements of the array after sorting    
print("Elements of array sorted in ascending order: ");    
for i in range(0, len(arr)):    
    print(arr[i], end=" ")
