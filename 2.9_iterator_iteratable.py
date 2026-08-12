'''
9. Write a program to demonstrate iterators and
iterables in Python.
'''

numbers = [10, 20, 30, 40, 50]

print("Iterable:", numbers)

it=iter(numbers)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
