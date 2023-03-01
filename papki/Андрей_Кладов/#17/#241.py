a=[int(x) for x in open('17-1.txt')]
a1=[]
sr=sum(a)/len(a)
for i in range(len(a)-2):
    if (int(a[i]<sr) + int(a[i+1]<sr) + int(a[i+2]<sr))>=2 and (int('5' in str(a[i])) + int('5' in str(a[i+1])) + int('5' in str(a[i+2])))>=2:
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))