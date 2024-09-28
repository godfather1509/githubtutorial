def fibonnaci(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)

a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
print(a+b)
print("Hello This is Git and GitHub tutorial")
print(fibonnaci(a))