with open("17-243.txt") as f:
    a = [int(x) for x in f]
soom=0
for x in a:
	if x%49==0:
		for i in str(x):
			soom+=int(i)
cnt=0
mix=1000000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1>soom and n2%10==7 and n2<=soom) or (n1%10==7 and n2>soom and n1<=soom):
			cnt+=1
			mix=min(mix,n1+n2)
print(cnt,mix)