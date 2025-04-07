s = "Hello world!"
s2 = ''

for i in range(len(s) - 1, -1, -1):
    s2 += s[i]

#Waste of memory
print(s2)