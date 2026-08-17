def remove(l, word):
    n = []
    for i in l:
        if not(i == word):
            n.append(i.strip(h))
    return n
l = ["  hello", "world  ", "  python  ", "Hello"]
h = "llo"
print(remove(l,h))