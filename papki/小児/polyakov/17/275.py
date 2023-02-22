a=[int(x) for x in open("17-275.txt")]
cnt=0
mix=-20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	soom=abs(n1)+abs(n2)
	if soom%11==0:
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)