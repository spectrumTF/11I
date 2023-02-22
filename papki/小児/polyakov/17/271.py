a=[int(x) for x in open("17-271.txt")]
avg=sum(a)/len(a)
cnt=0
mix=-20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if int(str(n1)[-1:])+int(str(n2)[-1:])==7:
			cnt+=1
			if n1<avg and n2<avg:
				mix=max(n1+n2,mix)
print(cnt,mix)