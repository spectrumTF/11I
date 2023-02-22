with open('17-328.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
a2=[x for x in a if x%50==0]
sr=sum(a2)/len(a2)
for i in range(len(a)-2):
    a3=[a[i]+a[i+1],a[i]+a[i+2],a[i+1]+a[i+2]]
    if int(a3[0]**0.5)==a3[0]**0.5 and int(a3[1]**0.5)==a3[1]**0.5 and int(a3[2]**0.5)==a3[2]**0.5 and min(a3[0],a3[1],a3[2])>sr :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),min(a1))