a = int(input("Enter the number you want to find the factorial of: "))
sum = 1
for i in range(1, a+1):
    sum *= i

print(sum)