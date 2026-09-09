n = int(input("enter the table you want to print"))
s = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(str(s) + "\n")