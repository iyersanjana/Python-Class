import os
fname = input("Enter a filename: ").strip()
infile = open(fname, "r")
string=infile.read()
cursor=0
def printf(string,cursor):
	left_part=string[:cursor]
	right_part=string[cursor:]
	print(left_part,"|",right_part)
	return
def cmd_h(string,cursor):
	if(cursor!=0):
		return cursor-1
	else:
		return 0
def cmd_i(string,cursor):
	if(cursor!=len(string)-1):
		return cursor+1
	else:
		return len(string)-1
def cmd_j(string,cursor):
	left_part=string[:cursor]
	right_part=string[cursor:]
	newstring=left_part+"|"+right_part
	print(newstring)
	f_line=newstring.find("\n",0,cursor)
	if (f_line==-1):
		print(newstring)
	else:
		l_line=newstring.rfind("\n",0,cursor)
		p_line=newstring.rfind("\n",0,l_line)
		n_pos=cursor-l_line
		n_cursor=p_line+n_pos
		left_part=string[:n_cursor]
		right_part=string[n_cursor:]
		newstring=left_part+"|"+right_part
		print(newstring)
		return
def cmd_k(string,cursor):
	left_part=string[:cursor]
	right_part=string[cursor:]
	f_string=left_part+"|"+right_part
	l_line=f_string.find("\n",cursor,len(f_string))
	if (l_line==-1):
		print(f_string)
	else:
		p_line=newstring.rfind("\n",0,l_line)
		n_cursor=cursor-p_line
		f_cursor=(l_line+n_cursor)
		left_part=string[:f_cursor]
		right_part=string[f_cursor:]
		f_string=left_part+"|"+right_part
		return
def cmd_x(string,cursor):
	left_part=string[:cursor-1]
	right_part=string[cursor:]
	print(left_part,"|",right_part)
	return
def cmd_d(string,cursor,text):
	text=text[:cursor]
	print(text)
	return
def cmd_dd(string,cursor):
	if(y<len(string)):
		List.remove(string[:cursor])
		return
def cmd_ddp(string,cursor,z):
	z=string[cursor:]
	string[cursor:]=string[cursor+1:]
	string[cursor+1:]=z
	return string[cursor:],string[cursor+1:]
def cmd_n(string,cursor,search):
	pos=string.find(search,cursor,len(string)-1)
	output=print(string[ :pos]+"|"+string[pos: ])
	return
def cmd_wq(string,cursor,output):
    new_file = open("op.txt",'a+')
    temp = start
    while temp!= None:
        new_file.write(temp[data]+"\n")
        temp = temp[n_ptr]
    new_file.close()

output={}
cmd_h(string,cursor)
cmd_i(string,cursor)
cmd_j(string,cursor)
cmd_k(string,cursor)
cmd_x(string,cursor)
cmd_d(string,cursor,text)
cmd_dd(string,cursor)
cmd_ddp(string,cursor,z)
cmd_n(string,cursor,"ugly")
cmd_wq(string,cursor)