#forma 1
def countBits(n):
while(n>0):
	if n%2: #verifica bit 1 ou zero
		count += 1
	n//=2 #reduz n por 2
	return count

#forma 2
def countBits(n):
    return bin(n).count("1")
