def sum_of_n_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter a number: "))
print("The sum of the first", n, "natural numbers is", sum_of_n_natural_numbers(n))