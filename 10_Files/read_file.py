# precte cely soubor
f = open('data.txt')
f.read()
f.close()

# precte prvni dva radky a pomoci .rstrip("\n") odstrani "\n"
f = open('data.txt')
a = f.readline().rstrip("\n")
b = f.readline().rstrip("\n")
f.close()

print(a)
print(b)

