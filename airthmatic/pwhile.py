n=1
while n<=100:
    count=0
    i=2
    while i<=n//2:
        if n%i==0:
            count+=1
            break
        i+=1
    if count==0 and n!=1:
        print(n,end=" ")
    n+=1