a=[int(x) for x in open('17-1.txt')]
a1=[]
s=[x for x in a if abs(x)%15==0 and x>0]
for i in range(len(a)-1):
    sr=(a[i]+a[i+1])//2
    if  abs(a[i])%2==1 and abs(a[i+1])%2==1 and sr>=min(s):
        a1.append(sr)
print(len(a1),min(a1))