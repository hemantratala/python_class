my_list = [1,2,2,3,1,4,5,1,2,6]
myFinallist = []
for i in my_list:
    if i not in myFinallist:
     myFinallist.append(i)
print(list(myFinallist))