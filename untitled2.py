v="Simon Peter John"
z=v.split(' ')
z1=z[0]
z2=z[1]
z3=z[2]
b1=(z1[0][0])
b2=(z2[0][0])
b3=(z3[0][0])

a1=["*"for i in z1[1:]]
s1="".join(a1)

a2=["*"for i in z2[1:]]
s2="".join(a2)

a3=["*"for i in z3[1:]]
s3="".join(a3)

y=[]
y.append(b1+s1)
y.append(b2+s2)
y.append(b3+s3)
print(y)

###########################

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