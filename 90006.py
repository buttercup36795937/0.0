string= 'I love you'
a= string.split(' ')
print(a)

################################

b= string[::-1]
s= b.split(' ')
print(s)

################################
n="I Love you so much"
c="so "*100
print(n.replace("so",c))

################################
import random
d=random.randint(1,100)
m="I Love you so much"
f= str("so "*d)
print(m.replace("so",f))
