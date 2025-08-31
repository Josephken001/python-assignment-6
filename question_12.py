# Question 12
def task12_is_prime(n):
    """
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
    """
    if n <= 1:
	    return False
    for i in range(2, int(n**0.5)+ 1):
	    if n % i == 0:
		    return False 
    return True 
print(task12_is_prime(7)) # True 
print(task12_is_prime(10)) # False


