a=[int(x) for x in open("17-243.txt")]
soom=0
for x in a:
	if x%61==0:
		for i in str(x):
			soom+=int(i)
cnt=0
mix=100000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1>soom and n2<=soom and n2%100==33) ^ (n2>soom and n1<=soom and n1%100==33):
			cnt+=1
			mix=min(mix,n1+n2)
print(cnt,mix)