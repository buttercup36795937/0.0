data1= input('請輸入a值')
data2= input("請輸入b值")
data3= input("請輸入c值")


a=(float(data1))
b=(float(data2))
c=(float(data3))

x=(b*b-4*a*c)
if x<=0:
    print("無解")

else:
     d=(-b+(b*b-4*a*c)**0.5)/(2*a) 
     e=(-b-(b*b-4*a*c)**0.5)/(2*a)  
     print("x1=",d,"x2=",e)
