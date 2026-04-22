def calculate_simple_interest(P, T, R):
    return (P * T * R) / 100

P = float(input("Enter the principal amount: "))
T = float(input("Enter the time period: "))
R = float(input("Enter the rate of interest: "))
print("The simple interest is", calculate_simple_interest(P, T, R))