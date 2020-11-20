#Capitalizes the first letter of each word in a string in Python
def capitalize(text):
    return  ' '.join(word[0].upper() + word[1:] for word in text.split())
# main code 
str1 = "Hello world!"
str2 = "hello world!"
str3 = "HELLO WORLD!"
# printing
print("str1: ", str1)
print("str2: ", str2)
print("str3: ", str3)
print()
print("capitalize(str1): ", capitalize(str1))
print("capitalize(str2): ", capitalize(str2))
print("capitalize(str3): ", capitalize(str3))
