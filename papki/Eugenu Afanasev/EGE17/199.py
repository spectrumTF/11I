a = [int(x) for x in open("17-199.txt")]
c = []
count=0
for i in range(len(a)-2):
    if not(a[i]>0 and a[i]%2==0 and len(str(a[i]))==2) and (a[i+1]>0 and a[i+1]%2==0 and len(str(a[i+1]))==2) and not(a[i+2]>0 and a[i+2]%2==0 and len(str(a[i+2]))==2):
        count+=1
        c.append(a[i]+a[i+1]+a[i+2])
print(c,max(c))
