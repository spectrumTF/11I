a=[int(x) for x in open("17-9.txt")]
cnt=0
mix=0
for i in range(len(a)-2):
	n1=bin(a[i])[2:]
	n2=bin(a[i+1])[2:]
	n3=bin(a[i+2])[2:]
	if int(n1.count("1")==2 and n1.count("0")>=1) + int(n2.count("1")==2 and n2.count("0")>=1) + int(n3.count("1")==2 and n3.count("0")>=1)>=2:
		cnt+=1
		mix+=max(a[i],a[i+1],a[i+2])
print(cnt,mix)