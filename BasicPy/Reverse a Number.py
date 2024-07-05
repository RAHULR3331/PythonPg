n=int(input("Enter the number"))
nr=0
while n%10!=0:
    c=n%10
    nr=nr*10+c
    n=n//10
print(nr)