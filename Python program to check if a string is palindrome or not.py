#Python program to check if a string is palindrome or not
# function to check palindrome string
def isPalindrome(string):
     rev_string = string[::-1]
     return string == rev_string
# Main code
x = "Google"
if isPalindrome(x):
     print(x,"is a palindrome string")
else:
     print(x,"is not a palindrome string")  
x = "ABCDEDCBA"
if isPalindrome(x):
     print(x,"is a palindrome string")
else:
     print(x,"is not a palindrome string")
x = "RADAR"
if isPalindrome(x):
     print(x,"is a palindrome string")
else:
     print(x,"is not a palindrome string")


x = "MADAM"
if isPalindrome(x):
     print(x,"is a palindrome string")
else:
     print(x,"is not a palindrome string") 

