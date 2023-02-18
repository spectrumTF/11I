a=[int(x) for x in open("17-7.txt")]
mix=0
cnt=0
for i in range(len(a)-2):
	if int(a[i]%3==2) + int(a[i+1]%3==2) + int(a[i+2]%3==2)>=1:
		cnt+=1
		mix+=min(a[i],a[i+1],a[i+2])
print(cnt,mix)