mix=10000
for N in range(1,1000):
	t=N
	n=""
	while t>0:
		n=str(t%4)+n
		t//=4
	if N%2!=0:
		n="2"+n+"11"
	else:
		n="13"+n+"02"
	R=int(n,4)
	if R>1000 and R<mix:
		mix=R
print(mix)