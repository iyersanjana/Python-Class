import os

data = 0; n_ptr = 1; p_ptr = 2
curr_ptr = None
curr_post = 0
cur_symbol = "^"
fname = input("Enter a filename: ")
infile = open(fname, "r")
List=infile.read()
fname.close()
List = List.split("\n")

def construct_doubly_linked_list(List):
    start = None; end = None
    for x in List:
        next_node = getNode(x)
        if start is not None:
            end[n_ptr] = next_node
            next_node[p_ptr] = end
            end = next_node
        else:
            start = next_node
            end = next_node
    return start, end

start, end = construct_doubly_linked_list(List)
curr_ptr = start[n_ptr]
display()

def getNode(info):
    return [info, None, None]

def display():
    global curr_post
    global curr_ptr
    global cur_symbol
    temp = start
    print()
    while temp!= None:
        if temp == curr_ptr:
            print(temp[data][: curr_post] + cur_symbol + temp[data][curr_post :])
        else:
            print(temp[data])
        temp = temp[n_ptr]
    return
    
#cmd_h: move cursor one character to the left 
def cmd_h():
    global curr_ptr
    global curr_post
    if curr_post == 0 and curr_ptr == start:
        pass
    else:
        if curr_post == 0:
            curr_ptr = curr_ptr[p_ptr]
            curr_post = len(curr_ptr[data])
        else:
            curr_post = curr_post - 1
    display()

#cmd_i: move cursor one character to the right
def cmd_i():
    global curr_ptr
    global curr_post
    if curr_post == len(end[data]) and curr_ptr == end:
        pass
    else:
        if curr_post == len(curr_ptr[data]):
            curr_ptr = curr_ptr[n_ptr]
            curr_post = 0
        else:
            curr_post = curr_post + 1
    display()
    
#cmd_j: move cursor vertically one line up 
def cmd_j():
    global curr_ptr
    global curr_post
    if curr_ptr == start:
        pass
    else:
        if len(curr_ptr[data][:curr_post]) > len(curr_ptr[p_ptr][data]):
            curr_post = len(curr_ptr[p_ptr][data])
        curr_ptr = curr_ptr[p_ptr]
    display()

#cmd_k: move cursor vertically one line down 
def cmd_k():
    global curr_ptr
    global curr_post
    if curr_ptr == end:
        pass
    else:
        if len(curr_ptr[data][:curr_post]) > len(curr_ptr[n_ptr][data]):
            curr_post = len(curr_ptr[n_ptr][data])
        curr_ptr = curr_ptr[n_ptr]
    display()

#cmd_x: delete the character to the left of the cursor 
def cmd_x():
    global curr_ptr
    global curr_post
    global end
    if curr_post == 0 and curr_ptr == start:
        pass
    else:
        if curr_post == 0:
            curr_post = len(curr_ptr[p_ptr][data])
            curr_ptr[p_ptr][data] = curr_ptr[p_ptr][data] + curr_ptr[data]
            curr_ptr[p_ptr][n_ptr] = curr_ptr[n_ptr]
            if curr_ptr != end:
                curr_ptr[n_ptr][p_ptr] = curr_ptr[p_ptr]
            else:
                end = curr_ptr[p_ptr]
            curr_ptr = curr_ptr[p_ptr]
        else:
            curr_ptr[data] = curr_ptr[data][:curr_post - 1] + curr_ptr[data][curr_post:]
            curr_post = curr_post - 1
    display()

#cmd_d: remove on current line from cursor to the end 
def cmd_d():
    global curr_ptr
    global curr_post
    curr_ptr[data] = curr_ptr[data][:curr_post]
    display()
            
#cmd_dd: delete current line and move cursor to the beginning of next line
def cmd_dd():
    global curr_ptr
    global curr_post
    if curr_ptr == end:
        pass
    else:
        curr_post = 0
        curr_ptr[p_ptr][n_ptr] = curr_ptr[n_ptr]
        curr_ptr[n_ptr][p_ptr] = curr_ptr[p_ptr]
        curr_ptr = curr_ptr[n_ptr]
    display()

#cmd_ddp: transpose two adjacent lines 
def cmd_ddp():
    global curr_ptr
    global curr_post
    global start
    global end
    
    if curr_ptr == end:
        pass
    else:
        temp = curr_ptr[data]
        curr_ptr[data] = curr_ptr[n_ptr][data]
        curr_ptr[n_ptr][data] = temp
        curr_ptr = curr_ptr[n_ptr]
    cmd_j()
    display()

#cmd_n: search for next occurrence of a string
def cmd_n():
    global curr_ptr
    global curr_post
    search_str = input("Enter the search string: ")
    temp = curr_ptr
    while temp!= None:
        if temp == curr_ptr:
            search_pos = temp[data].find(search_str, curr_post, len(temp[data]))
        else:
            search_pos = temp[data].find(search_str)
        if search_pos >= 0:
            curr_ptr = temp
            curr_post = search_pos
            break
        temp = temp[n_ptr]
    display()

#cmd_r: search backwards for next occurrence of a string
def cmd_r():
    global curr_ptr
    global curr_post
    search_str = input("Enter the search string: ")
    temp = curr_ptr
    while temp!= None:
        if temp == curr_ptr:
            search_pos = temp[data].rfind(search_str, 0, curr_post)
        else:
            search_pos = temp[data].rfind(search_str)
        if search_pos >= 0:
            curr_ptr = temp
            curr_post = search_pos
            break
        temp = temp[p_ptr]
    if search_pos < 0:
        print("Search string '", search_str, "' not found")
    display()

#cmd_t: transpose two characters
def cmd_t():
    global curr_ptr
    global curr_post
    if curr_post == 0 or curr_post == len(curr_ptr[data]):
        pass
    else:
        curr_ptr[data] = curr_ptr[data][: curr_post - 1] + curr_ptr[data][curr_post + 1] + curr_ptr[data][curr_post - 1] + curr_ptr[data][curr_post + 1:]
    display()

#cmd_plus: go to the beginning of next line
def cmd_plus():
    global curr_ptr
    global curr_post
    if curr_ptr == end:
        pass
    else:
        curr_post = 0
        curr_ptr = curr_ptr[n_ptr]
    display()

#cmd_insert: insert a string at the cursor
def cmd_insert():
    global curr_ptr
    global curr_post
    insert_str = input("Enter string to be inserted: ")
    curr_ptr[data] = curr_ptr[data][:curr_post] + insert_str + curr_ptr[data][curr_post:]
    curr_post = curr_post + len(insert_str)
    display()

#cmd_sub: substitute replace the character at the cursor with another one
def cmd_sub():
    global curr_ptr
    global curr_post
    rep_char = input("Enter the replacement character: ")
    curr_ptr[data] = curr_ptr[data][:curr_post - 1] + rep_char + curr_ptr[data][curr_post:]
    display()

#cmd_wq: write your representation as text file and save it 
def cmd_wq():
    new_file = open("output.txt",'a+')
    temp = start
    while temp!= None:
        new_file.write(temp[data]+"\n")
        temp = temp[n_ptr]
    new_file.close()