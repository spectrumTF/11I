Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=[int(x) for x in open("17-9.txt")]
c=0
m=0
for i in range(len(n)-2):
	n1=bin(a[i])[2:]
	n2=bin(a[i+1])[2:]
	n3=bin(a[i+2])[2:]
	if int(n1.count("1")>=3 and n1.count("0")>=1) + int(n2.count("1")>=3 and n2.count("0")>=1) + int(n3.count("1")>=3 and n3.count("0")>=1)>=2:
		c+=1
		m=max(m,n[i],n[i+1],n[i+2])
print(c,m)
