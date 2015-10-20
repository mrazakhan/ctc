#Reverse a null terminated string

def reverse(a,b):
	temp=a
	a=b
	b=temp
	return (a,b)

def reverse_str(st):
	st=list(st[:])
	l=len(st)-1 
	i=0
	while(i<l/2):
		a,b=reverse(st[i],st[l-i])
		st[i]=a
		st[l-i]=b
		i+=1
	return ''.join(st)

if __name__=='__main__':
	input='hello\n'
	output=reverse_str(input)
	print input, ' ', output
