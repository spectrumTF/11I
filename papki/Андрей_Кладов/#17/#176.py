a=[int(x) for x in open('17-4.txt')]
#b=[bin(x)[2:] for x in a]
s=[]
su=0
for i in range(len(a)):
    b=a[i]%10 +(a[i]//10)%10
    if b>14 and a[i]%3!=0 and a[i]%4!=0 and a[i]%7!=0:
        s.append(a[i])
        su+=a[i]
print(min(s),su)