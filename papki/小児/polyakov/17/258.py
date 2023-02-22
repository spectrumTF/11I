a = [int(x) for x in open("17-257.txt")]
arrX=[]
arrY=[]
for z in a:
	if z%2==0:
		arrX.append(z)
	if z%2!=0:
		arrY.append(z)
if max(arrX)>max(arrY):
	print(len(arrX),min(arrX))
else:
	print(len(arrY),min(arrY))