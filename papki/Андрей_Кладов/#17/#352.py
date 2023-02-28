f=[int(x) for x in open('17-352.txt')]
kr73=[int(x) for x in f if (int(x)%73==0) and len(str(x))>1]
mi73=10000
for x in f:
    if x%73==0 and mi73>x:
        mi73=x
a=[]
for i in range(len(f)-1):
    kr73pi=kr73
    kr73pi.append(f[i])
    kr73pi.append(f[i+1])
    if min(kr73pi)!=f[i] and min(kr73pi)!=f[i+1]:
        a.append(f[i]+f[i+1])
    #else:
        #print('/')
print(len(a),max(a))
