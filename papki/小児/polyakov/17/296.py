a=[int(x) for x in open("17-296.txt")]
cnt=0
mix=-20000
weirdsum=0
for i in a:
	weirdsum+=int(str(abs(i))[:1])
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if n1*n2>weirdsum:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)