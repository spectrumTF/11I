def check(x):
	x=oct(x)[2:]
	for i in x:
		if int(i)%2!=0:
			return 0
	return 1

def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ

a=[int(x) for x in open("17-328.txt")]
cnt=0
mix=20000
s=[int(x) for x in open("17-328.txt") if int(x)%22==0]
summ=0
for x in s:
	summ+=nm(x)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if check(n1+n2) and check(n2+n3) and check(n1+n3) and (n1+n2+n3)<summ:
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)