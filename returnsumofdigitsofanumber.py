def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total
n = int(input("Enter a number: "))
print("The sum of the digits of the number is", sum_of_digits(n))