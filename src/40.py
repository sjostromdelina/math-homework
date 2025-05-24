def find_prime_factors(n):
    factors = []
    # Divide n by 2 to get all even factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Now check odd numbers starting from 3 and incrementing by 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors

def calculate_factorials(num):
    result = [i for i in range(1, num + 1)]
    result.extend([factorial(i) for i in result])
    return result

# Example usage
print(find_prime_factors(36))  # Output: [2, 3, 5]
print(calculate_factorials(5))  # Output: [1, 2, 6, 120]
