import math
n=int(input("Enter a number: "))
root=math.sqrt(n)
if root*root==n:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
