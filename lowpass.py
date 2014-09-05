#simple: y(n) = x(n) + x(n-1) + x(n-2) + ...
def simple(x):
	return sum(x)/float(len(x))


def deriv(x):
	sum = 0
	for i in xrange(0,len(x)-1):
		sum = sum + x[i]-x[i+1]
	return sum/float(5)


