inFile = open("myfile.txt", "r+")
output = ""
for s in inFile:
    w = s[:-1]
    print(s[:-1])
    output = output+w
print(output)
inFile.close()

pizza1 = 2
if pizza1 == 3:
    print("pog")
elif pizza1 == 2:
    print("ok")
