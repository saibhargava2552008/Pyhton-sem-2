def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")