def decimalToRep(n,base):
	convertString = "0123456789ABCDEF"

	if n < base:
		return convertString[n]
	else :
		return decimalToRep(n//base,base) + convertString[n%base]

if __name__ == '__main__':
	print(decimalToRep(1453,2))
	print(decimalToRep(1453,3))
	print(decimalToRep(1453,8))
	print(decimalToRep(1453,16))
	print(decimalToRep(2,4))
