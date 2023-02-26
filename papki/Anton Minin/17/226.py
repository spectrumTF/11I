Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s=[int(x) for x in open('17-4.txt')]
a=[]
for i in range(len(s)-1):
    sr=sum(s)/len(s)
    if (s[i]<sr or s[i+1]<sr) and (str(s[i]).count('4')==0 and str(s[i+1]).count('4')==0):
        a.append((s[i]+s[i+1]))
print(len(a),min(a))