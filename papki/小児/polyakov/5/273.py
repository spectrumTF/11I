mix=0
for N in range(1,1000):
	n=bin(N)[2:]
	if N%2!=0:
		n="1"+n+"0"
	else:
		n="11"+n+"11"
	R=int(n,2)
	if R<126 and R>mix:
		mix=R
print(mix)