'''7. Write a program to demonstrate list dictionary
and set comprehensions. '''
#list
lst = [1,2,3,4,5]
squer_lst = [x ** 2 for x in lst]

print("list :",lst)
print("squer list :",squer_lst)

#dictionary

squer_dictionary = {x:x ** 2 for x in lst}
print("squer of dictionay :",squer_dictionary)

#set

squer_set = {x ** 2 for x in lst}
print("squer set :",squer_set)
