a = [int(x) for x in open("17-257.txt")]
arrX=[]
arrY=[]
for z in a:
	if z%11==0:
		arrX.append(z)
	if z%17==0:
		arrY.append(z)
if len(arrX)>len(arrY):
	print(len(arrX),min(arrX))
else:
	print(len(arrY),max(arrY))