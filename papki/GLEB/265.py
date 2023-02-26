with open("17-243.txt") as f:
    a = [int(x) for x in f]
soom=0
for x in a:
	if x%51==0:
		for i in str(x):
			soom+=int(i)
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1<soom or n2<soom):
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)