#15.11
def reverseDisplayHelper(a, high):
	if high <= 0:
		return ''
	else:
		l_index=high-1
	return a[l_index] + reverseDisplayHelper(a[:-1],l_index) 
def main():
	a = str(input("Enter the string: "))
	high=len(a)
	print("The reverse string is:",reverseDisplayHelper(a,high))
main()