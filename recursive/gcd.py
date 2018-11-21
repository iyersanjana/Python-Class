#15.3
def gcd(m,n):
	if (m % n ==0):
		return n
	else:
		return gcd(n, m % n)
def main():
	m=int(input("Enter an integer: "))
	n=int(input("Enter an integer: "))
	x=gcd(m,n)
	print("The GCD is:" ,x)
main()