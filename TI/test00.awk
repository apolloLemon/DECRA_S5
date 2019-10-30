$0					#print la ligne



"\n"

length($0) > 16
(length($0) > 16) {
	print "longeur",length($0),"mots", NF
}

{
	l += 1			#compter lignes
	w += NF			#compter mots
}
END {
	print l, w
}