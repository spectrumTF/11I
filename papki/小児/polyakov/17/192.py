a=[int(x) for x in open("17-7.txt")]
y=[]
for i in a:
	su=0
	for n in str(i):
		su+=int(n)
	if su%3==0:
		y.append(i)
print(len(y),max(y))