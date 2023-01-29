N=120
for M in range(1000):
    Ms=str(M)
    P1=2
    P2=1
    for i in range(len(Ms)):
        if (int(Ms[i])%2==0) and (Ms[i]!='0'):
            P1*=int(Ms[i])
        elif Ms[i]!='0':
            P2*=int(Ms[i])
    R=P1-P2
    if R<0:
        R*=-1
    if R==29:
        print(M)
        break
