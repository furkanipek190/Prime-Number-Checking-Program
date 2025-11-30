# 🧮 Prime Number Checking Program

A simple *Python project* that checks whether a given positive integer is *prime* or *not prime*.  
If the number is not prime, the program also lists *all divisors* in ascending order.

---

## 🎯 Purpose

This project helps beginners understand:

- Basic algorithm design  
- Pseudocode  
- Python conditional statements  
- Loops  
- Number theory logic (prime & composite numbers)

It demonstrates the full workflow from  
*Problem → Pseudocode → Python Code → Testing*.

---

## 🧠 Problem Definition

The user enters a positive integer.  
The program determines:

1. Whether the number is *prime*  
2. If not prime, the program lists *all numbers that divide it*

---

## 🔣 Pseudocode

1) Start

2) Ask user for a positive integer → n

3) If n ≤ 1 → print "not prime"

4) Create an empty divisor list

5) Loop from 1 to n  
   - If n % i == 0 → add i to divisor list

6) If divisor list contains *only 1 and n* → n is prime

7) Otherwise → n is not prime, show all divisors

8) End

---

## 🐍 Python Code

```python
# Prime Number Checking Program

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


🗂 Project Structure
Prime-Number-Checking-Program/
│
├── prime_number_checking_program.py
├── README.md
├── LICENSE
└── .gitignore


⚙ How to Run
python prime_number_checking_program.py


Developer
Furkan IPEK
📍 Türkiye
💬 Created as part of a beginner-level algorithm and Python learning project.