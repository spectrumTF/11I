f=[int(x) for x in open('17-353.txt')]
sr=(max(f)+min(f))/2
a=[]
for i in range((len(f))//2):
    if max(f[i],f[len(f)-1-i])>sr>min(f[i],f[len(f)-1-i]):
        a.append(f[i]+f[len(f)-1-i])
print(len(a),max(a))