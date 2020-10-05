v="Simon Peter John"
z=v.split(' ')
y=[]
for i in range(len(z)):
   j=["*"for i in z[i][1:]]
   y.append(z[i][0]+"".join(j))
print(y)
############################

a=['Company 1','Company 2','Company 3']
b=[]
for i in a:
    
    b.append(str(i).replace(" ","_"))
print(b)    
    
##########################
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    list2.append(str(i)+"$")
print(list2)    

########################
list3=[]
for i in list2:
    list3.append(str(i).replace('$',""))
print(list3)
########################
list1=[1,2,3,4]
list2=[5,6,7,8]
a=list(zip(list1,list2))
print(a)
#########################
s='I love you and you love him and who loves who'
a=s.split(' ')
keys=set(a)
b=sorted(keys)
values=[0 for i in b]
d={key: value for key,value in zip(b,values)}
for i in a:
    d[i]+=1
print(d)   

