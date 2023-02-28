a=[int(x) for x in open('17-1.txt')]
a1=[]
for i in range(len(a)-2):
    s=sum(a)/len(a)
    if ((a[i]<s and a[i+1]<s) or (a[i+1]<s and a[i+2]<s) or (a[i]<s and a[i+2]<s)) and ((abs(a[i])%10==8 and abs(a[i+1])%10==8) or (abs(a[i])%10==8 and abs(a[i+2])%10==8) or (abs(a[i+2])%10==8 and abs(a[i+1])%10==8)):
        a1.append(a[i]+a[i+1]+a[i+2])
print(len(a1),max(a1))