# Question 9
def task9_count_vowels(word):
    """
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
    """
    vowels = "aeiou"
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

print(task9_count_vowels("apple")) # 2
print(task9_count_vowels("banana")) # 3
