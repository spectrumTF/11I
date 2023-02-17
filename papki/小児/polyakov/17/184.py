a=[int(x) for x in open("17-5.txt")]
mix=0
cnt=0
for i in range(len(a)-1):
	if a[i]%2==0 or a[i+1]%2==0:
		cnt+=1
		mix=max(mix,a[i]+a[i+1])
print(cnt,mix)