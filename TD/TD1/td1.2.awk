awk -e ' (FNR==1) { print FILENAME " " $0 } ' T*txt

awk -e ' ((FNR==1)||(FNR==1))' { print FILENAME " " $0 } ' T*txt