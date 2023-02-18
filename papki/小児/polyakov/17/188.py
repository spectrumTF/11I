a=[int(x) for x in open("17-7.txt")]
mix=0
cnt=0
for i in range(len(a)-2):
	if int(a[i]%16==0) + int(a[i+1]%16==0) + int(a[i+2]%16==0)>=2:
		cnt+=1
		mix+=max(a[i],a[i+1],a[i+2])
print(cnt,mix)