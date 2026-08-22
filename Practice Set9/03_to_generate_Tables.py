def generateTables(n):
    tables = ""
    for i in range(1,11):
        tables += f"{n} X {i} = {n*i} \n"
    with open(f"tables/table{n}","w") as f:
        f.write(tables)


for i in range(2,21):
    generateTables(i)