# Data types and type casting

num = 10

price = 99.99

name = "Dharmesh"

male = True

print("Integer :",num,"Type :",type(num))
print("Float :",price,"Type :",type(price))
print("String :",name,"Type :",type(name))
print("Boolean :",male,"Type :",type(male))

#type casting

num_float = float(num)
print("Integer to float :",num_float,"Type :",type(num_float))

price_int = int(price)
print("Float to Ineger :",price_int,"Type :",type(price_int))

num_str = str(num)
print("Integer to String :",num_str,"Type :",type(num_str))

age = "21"
age_int = int(age)
print("String to Integer :",age_int,"type :",type(age_int))
