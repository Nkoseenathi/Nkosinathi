num_frogs = int(input('Enter the number of frogs:\n'))
num_toads = int(input('Enter the number of toads:\n'))
state = ['Frog']*num_frogs+['    ']+['Toad']*num_toads
correct=['Toad']*num_frogs+['    ']+['Frog']*num_toads
msg='Sorry, you\'ve lost.'
check=1

for i in range(1,len(state)+1):
    print("{:>4}".format(str(i)+'.'),end='')

print()

for i in range(0,len(state)):
    print(state[i],end='')

print() 

def _print():

    for i in range(1,len(state)+1):
        print("{:>4}".format(str(i)+'.'),end='')

    print()
    
    for i in range(0,len(state)):
        print(state[i],end='')

    print()
    
while True:
    user=input('>')
    if user=='quit':break
    user=int(user)-1
    ind=state.index('    ')

             
    if state[int(user)]=='Frog' and state[int(user)+1]=='    ' :
        state[int(user)+1]='Frog'
        state[int(user)]='    '

    if state[int(user)]=='Frog' and state[int(user)+1]!='    'and state[int(user)+2]=='    ':
        state[int(user)+2]='Frog'
        state[int(user)]='    '        
            
    if state[int(user)]=='Toad' and state[int(user)-1]=='    ' :
        state[int(user)-1]='Toad'
        state[int(user)]='    '

    if state[int(user)]=='Toad' and state[int(user)-1]!='    ' and state[int(user)-2]=='    ':
        state[int(user)-2]='Toad'
        state[int(user)]='    '     
    
    _print()
              
    if state==correct:
        print('Congratulations, you\'ve won!')
        break
    
    if ind-2>0 and ind+2<=len(state)-1:

        if (state[ind-1]==state[ind-2]) and (state[ind+1]==state[ind+2]):
            print(msg)
            break

        if (len(state)==5 and state[ind]=='    'and state[ind-1]==state[ind-2])and (state[ind]!=state[-1]) :
            print(msg)
            break

    if (state[0]=='    'and state[1]==state[2])or (state[-1]=='    'and state[-2]==state[-3]) :    
        print(msg)
        break 

    if (state[1]=='    'and state[2]==state[3]and state[0]!=state[3])or (state[-1]=='    'and state[-2]==state[-3]and state[0]!=state[3]) :
        print(msg)
        break
    
        