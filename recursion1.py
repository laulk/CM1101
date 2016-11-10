def count(i):
	print(i)
	i= i*2
	if i == 2048: return# >1024
	count(i)
#counts properly from 1,2-->1024 only if i = 1


def g(n):
	if n == 1 or n == 2:
		return 1
	else:
		return g(n-1)+g(n - 2)+ 1 # the +1 is to keep track number of times function called

