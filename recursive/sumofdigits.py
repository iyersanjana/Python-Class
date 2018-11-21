#15.1
def sumDigits(x):
	s=0
	if x == 0:
		return 0
	return (x%10) + sumDigits(x//10)
def main():
	x=int(input("Enter an integer: "))
	print("The sum of the digits is:" ,sumDigits(x))
main()