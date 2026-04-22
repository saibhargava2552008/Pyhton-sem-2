def is_palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    return rev == n
n = int(input("Enter a number: "))
if is_palindrome(n):
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")