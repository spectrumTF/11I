a=[int(x) for x in open("17-282.txt")]
cnt=0
mix=-20000
soom=-10000
for x in a:
	if x%41==0:
		soom=max(soom,x)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1+n2<soom:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)