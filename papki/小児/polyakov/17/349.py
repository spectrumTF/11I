from fnmatch import *
def nm(x):
	summ=1
	for i in str(x):
		summ*=int(i)
	return summ

a=[int(x) for x in open("17-346.txt")]
cnt=0
mix=-200000
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	sth=nm(n1)*nm(n2)*nm(n3)
	if sth<2*10**9 and fnmatch(str(sth),"83*8*"):
		cnt+=1
		mix=max(mix,sth)
print(cnt,mix)