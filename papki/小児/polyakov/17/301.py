def xor(x):
    xor_arr = 0
    for i in range(len(x)):
        xor_arr = xor_arr ^ x[i]
    return xor_arr
def nm(x):
	summ=0
	for i in str(x):
		summ+=int(i)
	return summ
a=[int(x) for x in open("17-301.txt")]
cnt=0
mix=-20000
mex=0
for i in a:
	if i%12==0:
		mex+=nm(i)
for i in range(len(a)-2):
	n1=a[i]
	n2=a[i+1]
	n3=a[i+2]
	a1=[n1%(nm(n2)+nm(n3))==0,n2%(nm(n1)+nm(n3))==0,n3%(nm(n2)+nm(n1))==0]
	if xor(a1) and (n1+n2+n3)<mex:
		cnt+=1
		mix=max(mix,n1+n2+n3)
print(cnt,mix)