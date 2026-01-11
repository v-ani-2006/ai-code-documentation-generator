# 1. Greet user
def greet(name):
    return f"Hello, {name}! Welcome to the Mini Toolkit."

# 2. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 3. Calculate factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# 4. Reverse a string
def reverse_string(s):
    return s[::-1]

# 5. Find maximum in a list
def max_in_list(lst):
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val

# 6. Calculate Fibonacci sequence up to n terms
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# 7. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 8. Check if a string is a palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# 9. Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# 10. Remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))


# ===== Example usage =====
if __name__ == "__main__":
    print(greet("Vani"))
    print("Is 17 prime?", is_prime(17))
    print("Factorial of 5:", factorial(5))
    print("Reverse of 'hello':", reverse_string("hello"))
    print("Max in list [3,7,2,9]:", max_in_list([3,7,2,9]))
    print("Fibonacci 10 terms:", fibonacci(10))
    print("Vowels in 'Python Programming':", count_vowels("Python Programming"))
    print("Is 'Racecar' palindrome?", is_palindrome("Racecar"))
    print("Sum of digits of 1234:", sum_of_digits(1234))
    print("Remove duplicates from [1,2,2,3,3,4]:", remove_duplicates([1,2,2,3,3,4]))
