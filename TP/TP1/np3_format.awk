function Capitalise( str ) {
	return toupper(substr(str,1,1)) tolower(substr(str,2))
}

/;/ {
	split($0, names, ";")
	family = toupper(names[2])
	n = split(names[1],names1," ") #slipts names[1] into given names, and puts the count in n
	givennames = ""
	
	for(i=1;i<=n;i++) {
		name = names1[i]
		dash = index(name,"-")
		if(dash==0){
			name = Capitalise(name)
		} else {
			name = Capitalise(substr(name,1,dash)) Capitalise(substr(name,dash+1))
		}
		givennames = givennames name " "
	}
	printf sprintf("%s %s\n",family, givennames)
}