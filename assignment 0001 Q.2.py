from tkinter import Y


value = input("Enter comma separated numbers:")
list = value.split (",")
tuple = tuple(list)
print('list:', list)
print('tuple:', tuple)