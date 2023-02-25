def f(x):
    d=0
    c=0
    c1=0
    while x!=0:
        if d%2==0:
            c1+=x%10
        else: 
            c+=x%10
        d+=1
        x//=10
    if c1>0:    
        return c%c1==0
#функция алины
a=[int(x) for x in open("17-343.txt")]
cnt=0
mix=200000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if f(n1) and f(n2) and f(n3):
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)