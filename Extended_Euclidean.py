import optparse
def extended_euclidean(a, m):

	u = 1
	v = 0
	x = 0
	y = 1
	r = 1
	
	while r != 0:
		r = a % m
		
		q = (a - r) / m
		s = u - q * v
		t = x - q * y
		
		a = m
		m = r
	
		u = v
		x = y
		
		v = s
		y = t
		
	return u

def main():
	parser = optparse.OptionParser('\nUsage: '+\
	'\nThis computes the modular inverse of a modulo m [e.g. (a)^-1 mod m]'+\
	'\n-a <specify a> ' +\
	'\n-m <specify m>')
	parser.add_option('-a', dest = 'a', type = int, help = 'specify a')
	parser.add_option('-m', dest = 'm', type = int, help = 'specify m')
	(options, args) = parser.parse_args()
	if options.a == None or options.m == None:
		print parser.usage
		exit(0)
	else:
		a = options.a
		m = options.m
	
	print "The inverse of %s modulo %s is %s" % (a,m,extended_euclidean(a, m))

if __name__ == '__main__':
	main()