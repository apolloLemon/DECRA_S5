v = [3,1,8,2,5]


def sommax(v):
	out = [v[0],1,1] #max
	for i in range(0,length(v)):
		if(v[i]==out[0]):
			out[1]+=1
		elif(v[i]>out[0]):
			out[1]=1
			out[0]=v[i]
			out[2]=i

