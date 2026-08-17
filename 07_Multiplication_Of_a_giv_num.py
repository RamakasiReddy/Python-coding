def table(n):
    n = int(input("Enter the number: "))
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

print(table(5))