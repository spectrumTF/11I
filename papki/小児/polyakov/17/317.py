def check(x,y):
    c=0
    while x!=0:
        if x%10!=y%10:
            c+=1
        x//=10
        y//=10
    return c==2
#функция алины
a=[int(x) for x in open("17-316.txt")]
cnt=0
mix=-20000
mex=0
#print(min(a))
#a.remove(1000)
#print(min(a))
#a.remove(1000)
#print(min(a))
#1000 1000 1001
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if ((check(n1,n2) and n1!=n2) or (check(n1,n3) and n1!=n3) or (check(n2,n3) and n2!=n3)) and (n1+n2+n3)>3001:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)