# Questiion 14
def task14_sum_list(numbers):
    """
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
    """
    total = 0 
    for num in numbers: 
	    total += num
    return total

print(task14_sum_list([1, 2, 3, 4])) #10
print(task14_sum_list([2, 2, 5, 2])) # 11


