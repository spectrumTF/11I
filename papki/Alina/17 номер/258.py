with open('17-257.txt') as f:
    a=[int(x) for x in f.readlines()]    
s=[x for x in a if x%2==0]
s1=[x for x in a if x%2==1]
if max(s)>max(s1):
    print(len(s),min(s))
else:
    print(len(s1),min(s1))