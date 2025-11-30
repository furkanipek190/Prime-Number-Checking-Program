# prime_number_checkin_program.py

# Get number from user
n = int(input("Enter a positive integer: "))

# Special case for numbers 1 and smaller
if n <= 1:
    print(f"{n} is not prime because prime numbers must be greater than 1.")
else:
    divisors = []  # List to hold divisors
    
    # Check all divisors from 1 to n
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    # If only 1 and n are divisors → prime
    if len(divisors) == 2:
        print(f"{n} is prime because it is divisible only by 1 and {n}.")
    else:
        # Sorting divisors for a logical order
        divisors_sorted = sorted(divisors)

        # Join with comma + space
        divisors_str = ", ".join(str(b) for b in divisors_sorted)

        print(f"{n} is not prime because it divides by the following numbers: {divisors_str}.")
