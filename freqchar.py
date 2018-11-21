#freq
	# Count each letter in the string
def countletters(line, counts):
	for ch in line:
		if ch.isalpha():
			counts[ord(ch) - ord('a')] += 1
	
def main():
	fname = input("Enter a filename: ").strip()
	infile = open(fname, "r") # Open the file
	counts = 26 * [0] # Create and initialize counts
	print("Char","\t","Freq","\t","%total")
	for line in infile: # Invoke the countLetters function to count each letter
		countletters(line.lower(), counts)
	total=0
	for i in range(len(counts)):
		total+=counts[i]
		total_percent=((counts[i])/total)*100
		if counts[i] != 0:				
			print(chr(ord('a') + i),"\t", str(counts[i]),"\t", total_percent)

	infile.close() # Close file

main()