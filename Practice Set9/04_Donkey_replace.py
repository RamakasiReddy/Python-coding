words =["Donkey", "ganda", "bad"]
with open("041_word.txt") as f:
    x = f.read()
for i in words:   
    x = x.replace(i,"#"*len(i))

with open("041_word.txt","w") as f:
    f.write(x)
