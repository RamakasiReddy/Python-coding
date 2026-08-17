def celsiustofarenheit(C):
    return (C * 1.8)+32
C = int(input("Enter the celcius: "))
a = celsiustofarenheit(C)
print(f"{a}F")