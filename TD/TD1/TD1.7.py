def conv (x, unit):
	if(unit=="cm"):
		unit="inch"
		x=x/2.54
	if(unit=="inch"):
		unit="cm"
		x=x*2.54