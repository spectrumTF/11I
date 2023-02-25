from collections import *

def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ

a=[int(x) for x in open("17-332.txt")]
cnt=0
mix=-20000
s=[int(x) for x in open("17-332.txt") if int(x)%17==0]
avg=sum(s)/len(s)
a1=[]
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	if nm(n1)==nm(n3) and n2<avg:
		cnt+=1
		a1.append(nm(n2))
print(cnt,Counter(a1).most_common(1))