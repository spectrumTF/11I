def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ
a=[int(x) for x in open("17-282.txt")]
cnt=0
mix=20000
soom=10000
for x in a:
	if x%37==0:
		soom=min(soom,x)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if nm(n1)==nm(soom) or nm(n2)==nm(soom):
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)