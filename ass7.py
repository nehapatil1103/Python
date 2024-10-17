try:
    a=int(input("enter number:"))
    b=int(input("enter number:"))
    c=a/b
except(ZeroDivisionError):
    print("Zero division not allowed")
