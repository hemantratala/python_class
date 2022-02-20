file=open("test.txt")
f=file.readlines()
f.pop()
f.append("Fourthline")
file.close()
file=open("test.txt","w")
for i in f:
    file.write(i)
file.close()
