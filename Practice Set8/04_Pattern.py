def pattern(n):
    if n == 0:
        return " end"
    print("*" * n)
    pattern(n - 1)
       
f = int(input("Enter the number of rows: "))
print(pattern(f))