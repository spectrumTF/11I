a=[int(x) for x in open("17-10.txt")]
cnt=0
mix=10000
for i in range(len(a)-1):
	su=a[i]+a[i+1]
	if len(str(su))==3:
		if (su%10)>(su%100//10):
			cnt+=1
			mix=min(mix,su)
print(cnt,mix)