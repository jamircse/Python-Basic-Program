#Python program to remove multiple elements from a list using list comprehension
# Python program to remove multiple elements 
# from a list using list comprehension
list1 = [10, 11, 20, 22, 30, 33, 40, 44, 50, 55, 60, 66, 70, 77, 80, 88, 90, 99]
# printing the list
print("The list is: ")
print(list1)
# list comprehension, removing elements
indices = 0, 2, 4, 6, 8, 10, 12, 14, 16
list1 = [i for j, i in enumerate(list1) if j not in indices]
# printing the list after removeing elements
print("After removing elements, list is: ")
print(list1)
