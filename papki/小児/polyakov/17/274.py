a=[int(x) for x in open("17-274.txt")]
cnt=0
minn=20000
for i in range(len(a)-1):
	n1=a[i]
	n2=a[i+1]
	soom=abs(n1)+abs(n2)
	if soom>17043 and soom%3==0:
			cnt+=1
			minn=min(minn,n1+n2)
print(cnt,minn)