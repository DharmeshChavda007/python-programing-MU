'''10.Write a program to extract specific information
from a text file using regular expressions. 
'''
import re

with open("data.txt", "r") as file:
    text = file.read()

emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)

phones = re.findall(r'\b\d{10}\b', text)

urls = re.findall(r'https?://[^\s]+', text)

print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)

print("\nURLs:")
for url in urls:
    print(url)
