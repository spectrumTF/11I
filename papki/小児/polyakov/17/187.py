a=[int(x) for x in open("17-6.txt")]
mix=0
cnt=0
for i in range(len(a)-2):
	if bin(a[i])[2:].count("1")==3 and bin(a[i+1])[2:].count("1")==3 and bin(a[i+2])[2:].count("1")==3:
		cnt+=1
		mix+=max(a[i],a[i+1],a[i+2])
print(cnt,mix)