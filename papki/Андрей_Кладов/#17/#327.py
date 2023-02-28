a=[int(x) for x in open('17-324.txt')]
a1=[]
a2=[x for x in a if x%37!=0]
sr=sum(a2)/len(a2)
for i in range(len(a)-2):
    if bin(a[i]+a[i+1]+a[i+2])[2:]==bin(a[i]+a[i+1]+a[i+2])[2:][::-1] and min(a[i],a[i+1],a[i+2])>sr :
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))