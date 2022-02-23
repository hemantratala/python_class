n=3
file=open("test.txt")
for i in range(n):
    print(file.readline())
file.close()