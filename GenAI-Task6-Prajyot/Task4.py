import os
file_name = input("enter the file name to search : ")
try:
    with open(file_name, "r")  as f:
        content = f.read()
        print(content)
except FileNotFoundError as FN:
    print(FN)
except PermissionError as PE:
    print(PE)
        