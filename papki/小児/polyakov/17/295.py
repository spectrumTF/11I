def nm(x):
	summ=1
	for i in str(x):
		summ*=int(i)
	return summ
a=[int(x) for x in open("17-295.txt")]
cnt=0
mix=-20000
maxx=max(a)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if nm(n1+n2)!=0 and (n1+n2)%nm(n1+n2)==0 and (n1+n2)<maxx:
		cnt+=1
		mix=max(mix,n1+n2)
print(cnt,mix)