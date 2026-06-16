try: 
    num = int(input("enter the numerator"))
    den = int(input("enter the denomerator"))
    result = num/den
except ZeroDivisionError:
    print("cannot happen")
except ValueError:
    print("Enter the valid integer")
except Exception as e:
    print(e)
else:
    print(f"result : {result}")
finally:
    print("Operation completed")