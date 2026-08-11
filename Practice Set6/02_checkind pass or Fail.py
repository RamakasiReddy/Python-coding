t = 720
a = int(input("Enter first  subject marks: "))
b = int(input("Enter second subject marksr: "))
c = int(input("Enter third  subject marks: "))

d = (a/t)*100
if d>=33 and d>40 and d<=100:
    print("You are pass in first subject")
elif d<0 or d>100:
    print("Invalid marks")
else:
    print("You are fail in first subject")
e = (b/t)*100
if e>=33 and e>40 and e<=100:
    print("You are pass in second subject")
elif e<0 or e>100:
    print("Invalid marks")
else:
    print("You are fail in second subject")
f = (c/t)*100
if f>=33 and f>40 and f<=100:
    print("You are pass in third subject")
elif f<0 or f>100:
    print("Invalid marks")
else:
    print("You are fail in third subject")

