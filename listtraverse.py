import os
fname = input("Enter a filename: ").split("\n")
infile = open(fname, "r")
List=infile.read()
x=0
y=0
def printf(List):
	left_part=List[0:y]
	right_part=List[x:]
	print(left_part,"|",right_part)
	return
def cmd_h(List):
	if(y>0):
		return List[:y-1]
	else:
		return 0
def cmd_i(List):
	if(y<len(List)):
		return List[:y+1]
	else:
		return len(List-1)
def cmd_j(List):
	if(x>0):
		return List[x-1:]
	else:
		return List[0:y]
def cmd_k(List):
	if(x<len(List)):
		return List[x+1:]
	else:
		return len(List-1)
def cmd_x(List):
	left_part=List[:y-1]
	right_part=List[x:]
	print(left_part,"|",right_part)
def cmd_d(List,output):
	output=output[:y]
	print(output)
def cmd_dd(List):
	if(y<len(List[x:y])):
		List.remove(List[:y])
def cmd_ddp(List,z):
	z=List[x:y]
	List[x:y]=List[x+1:y]
	List[x+1:y]=z
	return
def cmd_n(List,search):
	pos=List.find(search,List,len(List-1))
	if (pos>=0):
		List[x:y]=pos
		output=List[x:y]
def cmd_wq(List,output):
	fout= open("op1.txt","wt")
	fout.write(output)
	fout.close()

output=[]
cmd_h(List)
cmd_i(List)
cmd_j(List)
cmd_k(List)
cmd_x(List)
cmd_d(List,output)
cmd_dd(List)
cmd_ddp(List,z)
cmd_n(List,"ugly")
cmd_wq(List,output)