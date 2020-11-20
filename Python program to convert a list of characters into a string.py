#Python program to convert a list of characters into a string
list1 = ['J', 'e', 'r', 'r', 'y']
# printing characters list and its type
print("list1: ", list1)
print("type(list1): ", type(list1))
print()
# converting character list to the string
str1 = ""
for i in list1:
    str1 += i;
# print the string and its type
print("str1: ", str1)
print("type(str1): ", type(str1))
print('To Convert List ',list(str1))
