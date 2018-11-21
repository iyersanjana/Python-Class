#15.5
def m(i):
	if i == 0:
		return 0
	return (i/(2*i+1)) + m(i - 1)
def main():
	i=10
	print("The sum is:", m(i))
main()