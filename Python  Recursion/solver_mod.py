def make_state(num_frogs, num_toads):
    lst=['Frog']*num_frogs+['']+['Toad']*num_toads
    return lst

def find_space(state):
    st=state.index('')
    return st

def is_frog(state, index):
    if state[index]=='Frog':return True
    else:return False
    
def is_toad(state, index):
    if state[index]=='Toad':return True
    else:return False
    
def move(state, index):
    temp=state[index]
    i=state.index('')
    state[index]=''
    state[i]=temp
    return state

def print_state(state):
    print('|',end='')
    for i in state:
        if i=='':
            print('    ',end='|')
        else:
            print(i,end='|')
        
def is_win(state):
    f=[]
    t=[]

    for i in state:
        if i=="Frog":
            f.append('Frog')

        elif i=='Toad':
            t.append('Toad')

    win=t+['']+f 
    
    if state==win:return True
    else:return False
