try:
    marks = int(input("Enter your marks: "))
    result = marks / 0
    print("Your result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("The code excuted succesfully")
