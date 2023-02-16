a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if int(i%2==0)+int(i%3==0)+int(i%5==0)+int(i%7==0)==2:
		y.append(i)
print(len(y),max(y)+min(y))