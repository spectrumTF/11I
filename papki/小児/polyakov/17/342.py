a=[int(x) for x in open("17-342.txt")]
cnt=0
mix=200000
s1=[x for x in a if x%37==0]
s2=[x for x in a if x%73==0]
M1=min(s1)
M2=max(s2)
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (M2<n1<M1)^(M2<n2<M1):
		cnt+=1
		mix=min(mix,n1+n2)
print(cnt,mix)