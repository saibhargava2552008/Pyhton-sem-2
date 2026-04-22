def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome string")
else:
    print(s, "is not a palindrome string")
