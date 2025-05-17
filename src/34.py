import math

def calculate_power(base, exponent):
    result = base ** exponent
    return result

def main():
    print("Input numbers and operations: ")
    base_num1 = float(input("Enter first number (base): "))
    exponent1 = int(input("Enter second number (exponent): "))

    # Calculate power of the base raised to the exponent
    result = calculate_power(base_num1, exponent1)
    
    if isinstance(result, str):
        print(f"The calculation resulted in: {result}")
    else:
        print(f"The calculation resulted in: {base_num1}^{exponent1}")

if __name__ == "__main__":
    main()
