def divide(num1, num2):
    result = num1 / num2 if num2 != 0 else None
    print(f"{num1} / {num2} is equal to {result}" if num2 != 0 else "You cannot divide by 0.")
    return result