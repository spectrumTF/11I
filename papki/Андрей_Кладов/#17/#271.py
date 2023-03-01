a=[int(x) for x in open('17-271.txt')]
a1=[]
a2=[]
sr=sum(a)/len(a)
for i in range(len(a)-1):
    if (abs(a[i])%10+abs(a[i+1])%10)==7 :
        a1.append(a[i]+a[i+1])
        if a[i]<sr and a[i+1]<sr:
            a2.append(a[i]+a[i+1])
print(len(a1),max(a2))