n=int(input("Enter a number: "))
temp=n
sum=0
digit=len(str(n))
while temp>0:
    rem=temp%10
    sum=sum+rem**digit
    temp=temp//10   
if sum==n:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")
