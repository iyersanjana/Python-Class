class Encrypt:
	def __init__(self, newmsg = '',msg=''):
		self.__newmsg=newmsg
		self.__msg=msg

	def getnewmsg(self):
		return self.__newmsg

	def getmsg(self):
		return self.__msg

	def en(self):
		for ch in string:
			x = ord(ch)
			if ch == ' ':
				self.__newmsg += ' '
			else:
				self.__newmsg += chr(x+key)
		return self.__newmsg

	def de(self):
		for char in encryptmessage:
			y = ord(char)
			if char == ' ':
				self.__msg += ' '
			else:
				self.__msg += chr(y-key)
		return self.__msg

fname = input("Enter a filename: ").strip()
infile = open(fname, "r")
string=infile.read()
key = int(input('Enter a key (1-26):'))
Y=Encrypt()
encryptmessage=Y.en()
print('Your new message is: ', Y.en(),'\nYour original message is:\n', Y.de())