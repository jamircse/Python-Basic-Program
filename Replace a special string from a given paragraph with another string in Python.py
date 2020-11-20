#Replace a special string from a given paragraph with another string in Python
# importing the module
import re
# string
paragraph='''A computer programmer, sometimes called only programmer or more recently a coder, is a person who creates computer software. The term computer programmer can refer to a specialist in one area of computers, or to a generalist who writes code for many kinds of software.'''
# replacing string
reg=re.compile('programmer')
s=reg.sub("developer",paragraph)
# printing the replaced string
print(s)
