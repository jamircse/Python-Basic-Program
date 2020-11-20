#Python program to find total number of letters and digits
print("Input a string: ")
str1 = input()
no_of_letters, no_of_digits = 0,0
for c in str1:
   if (c>='a' and c<='z') or (c>='A' and c<='Z'):
       no_of_letters += 1
   if c>='0' and c<='9':
       no_of_digits += 1
print("Input string is: ", str1)
print("Total number of letters: ", no_of_letters)
print("Total number of Digits: ", no_of_digits)
