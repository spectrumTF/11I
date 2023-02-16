a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]
for i in range(len(a)):
    if (int(a[i]%2==0)+int(a[i]%3==0)+int(a[i]%5==0)+int(a[i]%7==0))==2:
        s.append(a[i])
print(len(s),min(s)+max(s))