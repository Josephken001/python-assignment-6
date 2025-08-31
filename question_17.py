# Question 17
def task17_palindrome_check(word):
    """
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
    """
    return word.lower() == word.lower()[::-1]

print(task17_palindrome_check("madam")) # True 
print(task17_palindrome_check("hello")) # False


