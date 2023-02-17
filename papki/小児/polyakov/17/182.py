a=[int(x) for x in open("17-4.txt")]
y=[]
for i in a:
	if i%13==7:
		if i%7!=0 and i%11!=0:
			y.append(i)
print(max(y)-min(y),len(y))