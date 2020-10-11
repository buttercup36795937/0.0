l1 = [1,2,3,4,5]
l2 = [6,5,4,3,2]
l3=[]

for x in range(len(l1)):
    if l1[x]>l2[x]:
        l3.append(l1[x])
    else:
        l3.append(l2[x])
        

print(l3)        
#####################
v1 = [1,2,3,4,5]
v2 = [6,5,4,3,2]
v3 = [False,False,True,False,True]
v4=[]

for i in range(len(v3)):
    if v3[i]== True:
        v4.append(v1[i])
    else:
        v4.append(v2[i])

print(v4)