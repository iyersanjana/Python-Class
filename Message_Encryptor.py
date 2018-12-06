class Encrypt:
	def __init__(self, newmsg = ''):
		self.__newmsg=newmsg

	def getnewmsg(self):
		return self.__newmsg

	def generate(self):
		for c in string:
			x = ord(c)
			if c == ' ':
				self.__newmsg += ' '
			else:
				self.__newmsg += chr(x+key)
		return self.__newmsg
  
fname = input("Enter a filename: ").strip()
infile = open(fname, "r")
string=infile.read()
key = input('Enter a key (1-26):')
key = int(key)
Y=Encrypt()
print('Your new message is: ', Y.generate())