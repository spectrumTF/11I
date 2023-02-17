a=[int(x) for x in open("17-5.txt")]
cnt=0
sumax=0
for i in range(len(a)-1):
	if abs(a[i])%10==7 or abs(a[i+1])%10==7:
		cnt+=1
		sumax=max(sumax,a[i]+a[i+1])
print(cnt,sumax)