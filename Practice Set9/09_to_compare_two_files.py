with open("011_poem.txt") as f:
    contenta = f.read()

with open("041_word.txt") as f:
    contentb = f.read()
if(contenta == contentb):
    print("yes these two files are same ")
else:
    print("no these two files are not same")