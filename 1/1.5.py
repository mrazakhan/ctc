import sys
def compress(st):
	lst=[]
	count=0
	for  i in range(len(st)):
		ch=st[i]
		if i==0:
			lst.append(ch)
			count+=1
		elif st[i-1]==ch:
			count+=1
		else:
			lst.append(str(count))
			count=1
			lst.append(ch)

	lst.append(str(count))
	return ''.join(each for each in lst)

if __name__=='__main__':
	st=sys.argv[1]
	out= compress(st)
	if len(out)>len(st):
		out=st
	print out

