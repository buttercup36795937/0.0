score=['小徐',5,9,6,8,7,10,6]
print(max(score[1:]))
print(min(score[1:]))
c=sorted(score[1:],reverse=True)
d=c[0:3]
print(d)
e=c[4:8]
print(e)
a=sum(score[1:])
b=len(score[1:])
print(int(a/b))
####################################
for x in range(1,10):
    for i in range(1,10):
        print('%ix%i=%2i' % (x, i, x*i), end=' ')
    print()
####################################

import random
d=random.randint(1,100)
s=str(" So"*d)
a="I love so much"
for i in a :
    if  i=="s":
         c =a.replace("so",s)
"".join(c.split())
print(c)