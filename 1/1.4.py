import sys
import os

def change_str(st):

	lst=[]
	i=len(st)-1
	while i>=0:
		if st[i]==' ':
			lst.insert(0,'%20')
		else:
			lst.insert(0,st[i])
		i-=1
	
	return ''.join(each for each in lst)

if __name__=='__main__':
	input=sys.argv[1]
	print change_str(input)
