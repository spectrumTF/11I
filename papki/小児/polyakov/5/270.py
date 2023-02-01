mix=10000
for N in range(1,1000):
	n=bin(N)[2:]
	if N%2!=0:
		n="10"+n+"11"
	else:
		n="1"+n+"00"
	R=int(n,2)
	if R>1023 and R<mix:
		mix=R
print(mix)