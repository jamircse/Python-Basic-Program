#Python program to find total number of uppercase and lowercase letters
print("Input a string: ")
str1 = input()
no_of_ucase, no_of_lcase = 0,0
for c in str1:
  if c>='A' and c<='Z':
    no_of_ucase += 1
  if c>='a' and c<='z':
    no_of_lcase += 1
print("Input string is: ", str1)
print("Total number of uppercase letters: ", no_of_ucase)
print("Total number of lowercase letters: ", no_of_lcase)
