def GreatestOfThree():
    a = int(input("Enter thre first num: " ))
    b = int(input("Enter thre second num: " ))
    c = int(input("Enter thre third num: " ))  

    if(a>b and a>c):
       return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    elif(a == b == c):
        return "All numbers are equal"
    else:
        return "Invalid input"
print(GreatestOfThree())

