a=[int(x) for x in open("17-1.txt")]
cnt=0
mix=0
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	avg=sum(a)/len(a)
	if (n1<avg or n2<avg) and ((n1%3==0 and n1%5!=0 and n1%11!=0 and n1%19!=0) or (n2%3==0 and n2%5!=0 and n2%11!=0 and n2%19!=0)):
			cnt+=1
			mix=max(mix,n1+n2)
print(cnt,mix)