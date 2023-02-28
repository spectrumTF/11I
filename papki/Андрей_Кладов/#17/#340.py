a=[int(x) for x in open('17-340.txt')]
a1=[]
s=[oct(x)[2:] for x in a]
s1=[x for x in a if x%22==0]
sr=sum(s1)/len(s1)
for i in range(len(a)-1):
    if  s[i].index(max(s[i]))<s[i].index(min(s[i])) and s[i+1].index(max(s[i+1]))<s[i+1].index(min(s[i+1])) and a[i]+a[i+1]<sr:
        a1.append(a[i]+a[i+1])
print(len(a1),max(a1))