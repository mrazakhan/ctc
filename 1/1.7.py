import random
import math
def ZM(M,N):
	matrix=[[random.randint(0,10) for x in range(M)] for y in range(N)]
	ret=[]
	for i in range(M):
		for j in range(N):
			if matrix[i][j]==0:
				ret.append(i)
	return matrix,ret

M=5
N=5
mat, ret= ZM(5,5)

print mat
print ret
for each in ret:
	print each
	for i in range(M):
		mat[each][i]=0
	for j in range(N):
		mat[j][each]=0



print mat
print ret

