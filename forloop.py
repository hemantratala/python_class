my_list = [1,2,1,5,9,5,6]
myFinallist = []
for i in my_list:
    if i not in myFinallist:
     myFinallist.append(i)
print(list(myFinallist))