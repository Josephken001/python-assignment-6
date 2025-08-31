# Question 16
def task16_factorial(n):
    """
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
    """
    result = 1
    for i in range(1, n+1):
	    result *= i
    return result

print(task16_factorial(5)) #120

