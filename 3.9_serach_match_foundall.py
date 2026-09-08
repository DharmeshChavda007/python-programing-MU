'''9. Write a program to use re module functions
such as match search and find all. 
'''
import re
txt = "hii my name is Dharmesh"
a = "hello"
b = "hell"
x = re.search("^hii.*Dharmesh$",txt)

if x:
    print("yes, we have a match.")
else:
    print("not found.")

y = re.match(a,b)

if y:
    print("yes, we have a match.")
else:
    print("not found.")


text = "apple banana mango apple orange"

result = re.findall(r'\ba\w*', text)

print(result)



