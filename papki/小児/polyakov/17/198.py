a=[int(x) for x in open("17-10.txt")]
cnt=0
mix=10000
for i in range(len(a)-1):
	su=a[i]+a[i+1]
	svn=""
	while su>0:
		svn=str(su%7)+svn
		su//=7
	if svn==svn[::-1]:
			cnt+=1
			mix=max(mix,int(svn))
print(cnt,mix)