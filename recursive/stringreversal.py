#15.9
def reverseDisplay(a):
    if len(a) == 0:
        return a
    return reverseDisplay(a[1:]) + a[0]

def main():
	a = str(input("Enter the string: "))
	print("The reverse string is:",reverseDisplay(a))
main()