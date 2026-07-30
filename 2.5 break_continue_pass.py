'''Write a program to demonstrate the use of
break continue and pass statements.'''

# break 

for i in range(5):
    if i == 3:
        print('loop end')
        break
    print(i)

print('========================================')

# continue

for i in range(10):
    if i == 6:
        continue
    print(i)

print('========================================')

# pass

for i in range(5):
    if i == 3:
        pass
    print(i)
print('End of program')

