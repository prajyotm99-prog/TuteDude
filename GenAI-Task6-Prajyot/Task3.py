def  check_age(age):
    if age <= 0:
        raise ValueError("cannot be negative or zero")
    elif age >= 120:
        raise ValueError("seems unrealistic")
    else:
        return ("Age is Valid")
try:
    age = int(input("enter the age"))
    print(check_age(age))
except ValueError as e:
    print(e)
