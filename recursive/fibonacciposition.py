#15.7
def fib(i):
	global count
	count += 1
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fib(i - 1) + fib(i - 2)
def main():
	global count
	count=0
	i = eval(input("Enter an index for a Fibonacci number: "))
	print("The Fibonacci number at index", i, "is", fib(i))
	print("The number of times fib is called:", count)
main()