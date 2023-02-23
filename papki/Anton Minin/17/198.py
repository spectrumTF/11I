Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=[int(x) for x in open("17-10.txt")]
c=0
m=10000
for i in range(len(an)-1):
        s=a[i]+a[i+1]
	sv=""
	while s>0:
		sv=str(s%7)+sv
		s//=7
	if sv==sv[::-1]:
                c+=1
		m=max(m,int(sv))
print(c,m)
