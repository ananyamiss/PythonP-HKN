def bet(a,b,c):
	return a<=b and b<=c

def retFuzzWeight(x,a,b,c,oneFAR,zeroFRR,EER,zeroFAR,oneFRR):
	if bet(oneFAR,x,zeroFRR):
		return a*(x-oneFAR)/(zeroFRR-oneFAR)
	else:
		if bet(zeroFRR,x,EER):
			return a+(c-a)*(x-zeroFRR)/(EER-zeroFRR)
		else:
			if bet(EER,x,zeroFAR):
				return c+(b-c)*(x-EER)/(zeroFAR-EER)
			else:
				if bet(zeroFAR,x,oneFRR):
					return b+(1-b)*(x-zeroFAR)/(oneFRR-zeroFAR)


def fuzz(a,b):
	return (a+b)/2