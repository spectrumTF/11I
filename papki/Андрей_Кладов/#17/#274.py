a=[int(x) for x in open('17-274.txt')]
a1=[]
for i in range(len(a)-1):
    if abs(a[i])+abs(a[i+1])>17043 and (abs(a[i])+abs(a[i+1]))%3==0:
        a1.append(a[i]+a[i+1])
print(len(a1),min(a1))