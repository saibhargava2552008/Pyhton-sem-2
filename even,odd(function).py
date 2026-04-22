def num(a):
    if a%2==0:
        return "Even"
    else:
        return "Odd"
n=int(input("Enter a number: "))
print(n,"is an",num(n),"number")