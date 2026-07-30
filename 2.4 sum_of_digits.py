'''Write a program to find the sum of digits of a
number using a while loop. '''

num = int(input("Enter a number: "))
t = num
sum = 0

while t > 0:
    digit = t % 10      
    sum = sum + digit     
    t = t // 10      

print("Sum of digits =", sum)
    
