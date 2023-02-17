a=[int(x) for x in open("17-5.txt")]
mix=0
cnt=0
for i in range(len(a)-1):
	if a[i]%10==5 and a[i+1]%10==5:
		cnt+=1
		mix=max(mix,a[i]+a[i+1])
print(cnt,mix)