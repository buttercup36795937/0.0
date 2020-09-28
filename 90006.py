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
        print('%dx%d=%2d' % (x, i, x*i), end=' ')
    print()
####################################
import random
d=random.randint(1,100)
a="I Love You"
b="much"
print(a,end=' ')
for i in range(d):
    c="so"
    print(c,end=' ')
print(b)