import random
print("guess the lucky number")
i=0
count=0
while i<=5:
    num=int(input("enter the number"))
    r=random.randint(1,5)
    i=i+1
    if num==r:
        count=count+1
    print("lucky number",r)
    if count==3:
        print("congrats u r lucky")
        break
if count<3:
    print("sorry try again")
