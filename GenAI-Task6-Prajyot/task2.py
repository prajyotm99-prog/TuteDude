price = [120, 350, 'abc', 500, -200, 800]
total_sum = 0

for i in price:
    try:
        if i < 0:
            continue  
        total_sum += i
        
    except TypeError as te:
        print(f"Skipping invalid item '{i}': {te}")

print(f"Final Sum: {total_sum}")