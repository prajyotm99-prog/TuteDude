class NegativePriceError(Exception):
    pass

cart = []

while True:
    user_input = input("Enter price (or 'q' to quit): ").strip().lower()
    
    if user_input == 'q':
        break
        
    try:
        price = float(user_input)
        
        if price < 0:
            raise NegativePriceError("Price cannot be negative.")
            
        cart.append(price)
        
    except ValueError:
        print("Invalid input. Please enter a number.")
        
    except NegativePriceError as e:
        print(e)

print(f"\nTotal items: {len(cart)}")
print(f"Total bill: {sum(cart):.2f}")
