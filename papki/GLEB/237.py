with open("17-1.txt") as f:
    a = [int(x) for x in f]
c=[]
count=0
s=sum(a)/len(a)
for i in range(len(a)-2):
    if ((a[i]<s and a[i+1]<s) or (a[i+2]<s and a[i+1]<s) or (a[i]<s and a[i+2]<s)) and ((abs(a[i])%19==0 and abs(a[i+1])%19==0) or (abs(a[i+1])%19==0 and abs(a[i+2])%19==0)or (abs(a[i])%19==0 and abs(a[i+2])%19==0)) :
        c.append((a[i]+a[i+1]+a[i+2]))
        count+=1
print(count,max(c))