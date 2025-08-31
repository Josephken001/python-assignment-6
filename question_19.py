# Question 19
def task19_find_min(numbers):
    """
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
    """
    smallest = numbers[0]
    for num in numbers:
	    if num < smallest:
		    smallest = num
    return smallest

print(task19_find_min([5, 10, 9, 20, 1])) # 1


