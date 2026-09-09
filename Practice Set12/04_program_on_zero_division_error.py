try:
    a = int(input("enter first number"))
    b = int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError as t:
    print("infinite")