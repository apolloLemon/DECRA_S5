INTERVAL_DEB 	= 1
INTERVAL_FIN 	= 10
INTERVALS		= 11

#out=[]
#def xi (a,b,n,i):
#	return a+(i-1)*((b-a)/(n-1))
#for i in range(1,11+1):
#	out.append(xi(1,10,11,i))


def lesXi1(a,b,n) :
	xi = [ a + (b-a)*(i-1)/(n-1) for i in range(1,n+1) ]
	return( xi )

print lesXi1(1,10,11)

