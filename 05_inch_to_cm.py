def cm(n):
    if n == 0:
        return 0
    return(f"{n * 2.54} cm")

n = int(input("Enter the number of inches: "))
print(cm(n))
