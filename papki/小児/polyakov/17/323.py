def chc10(x):
	tg=0
	for i in range(10):
		if str(i) in str(x):
			tg+=1
	return tg==10
def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ
a=[int(x) for x in open("17-316.txt")]
cnt=0
mix=20000
summ=0
for x in a:
	summ+=nm(x)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if chc10(n1*n2*n3) and n1+n2+n3<summ:
		cnt+=1
		mix=min(mix,n1+n2+n3)
print(cnt,mix)