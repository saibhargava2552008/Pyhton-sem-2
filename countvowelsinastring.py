def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count
s = input("Enter a string: ")
print("The number of vowels in the string is", count_vowels(s))