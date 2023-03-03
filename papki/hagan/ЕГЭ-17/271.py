a=[int(x) for x in open("17-243.txt")]
soom=0
s=[]
c=0
for x in a:
	if x%33==0:
		soom+=x
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	if (n1>soom or n2>soom):
		s.append(int(a[i])+int(a[i+1]))
print(len(s),min(s))