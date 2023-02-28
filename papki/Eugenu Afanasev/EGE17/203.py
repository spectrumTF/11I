a = [int(x) for x in open("17-202.txt")]
c = []
count=0
for i in range(len(a)-2):
    if not(a[i]>0 and a[i]%10==5 and len(str(a[i]))==3) and (a[i+1]>0 and a[i+1]%10==5 and len(str(a[i+1]))==3) and not(a[i+2]>0 and a[i+2]%10==5 and len(str(a[i+2]))==3):
        count+=1
        c.append(a[i]+a[i+1]+a[i+2])
print(count,max(c))
