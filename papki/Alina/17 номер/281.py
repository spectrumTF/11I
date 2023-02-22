with open('17-281.txt') as f:
    a=[int(x) for x in f.readlines()]
a1=[]
for i in range(len(a)-5):
    a2=sorted([a[i],a[i+1],a[i+2]])
    a3=sorted([a[i+3],a[i+4],a[i+5]])
    if ((a2[1]/a2[0]*a2[1]==a2[2] and (a3[1]-a3[0])+a3[1]==a3[2]) or (a3[1]/a3[0]*a3[1]==a3[2] and (a2[1]-a2[0])+a2[1]==a2[2])) and ((a2[1]/a2[0])==(a3[1]-a3[0]) or a3[1]/a3[0]==(a2[1]-a2[0])):
        a1.append(sum(a2)+sum(a3))
print(len(a1),max(a1))  