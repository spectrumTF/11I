mix=0
for N in range(1,1000):
	n=hex(N//2)[2:]
	if N%4!=0:
		n="F"+n+"A0"
	else:
		n="15"+n+"C"
	R=int(n,16)
	if R<65536 and N>mix:
		mix=N
print(mix)