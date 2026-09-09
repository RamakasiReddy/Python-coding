try:
    with open("1.txt" , "r") as f:
     print(f.read())
except Exception as t:
    print(t)
try:
    with open("2.txt" , "r") as f:
     print(f.read())
except Exception as t:
    print(t)
try:
    with open("3.txt" , "r") as f:
     print(f.read())
except Exception as t:
    print(t)
print("Than You")