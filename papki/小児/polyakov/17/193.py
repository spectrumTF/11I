def sus(x):
	su=0
	for n in str(x):
		su+=int(n)
	return su
a=[int(x) for x in open("17-8.txt")]
cnt=0
mix=0
for i in range(len(a)-1):
	ses1=sus(bin(a[i])[2:])
	ses2=sus(bin(a[i+1])[2:])
	if (ses1>5 and ses1%2!=0) or (ses2>5 and ses2%2!=0):
		cnt+=1
		mix=max(mix,a[i]+a[i+1])
print(cnt,mix)