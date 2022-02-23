n=int(input("guess the number"))
import random
r = random.randint(1,10)

if n==r:
    print("correct")
else:
    print("not correct")
