# Question 13

x = "Global Vairable"

def task13_scope_demo():
    """
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
    """
    x = "Local Vairable "
    print("Inside function:", x)

task13_scope_demo() # Inside function: local vairable 
print("Outside function:", x) # Outside function: Global vairable

