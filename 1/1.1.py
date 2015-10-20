# Is string unique
import sys

def process(input):

	isUnique=True
	for i in range(len(input)-1):
		for j in range(i+1,len(input)):
			print input[i], input[j]
			if input[i]==input[j]:
				isUnique=False
				break	
	return isUnique

if __name__=='__main__':
	print 	process(sys.argv[1])
	
