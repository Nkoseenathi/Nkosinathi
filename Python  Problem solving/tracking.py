animalNum=0
log={}
print('Please enter the animal identity codes. (Press return when done.)')
animalNum=0
animalCode='1'
sign=''
n=''
i=1
check=False
loop=False 
count=1
while True:
    
        
    if loop==False:
        while animalCode!=''and i>0:

            animalNum+=1
            animalCode=input('Animal no. '+str(animalNum)+':\n')
          
            if animalCode!='':
                log[animalCode]=""

            else:
                print('Commands: print, log <animal id> <x ord> <y ord>, quit.')

        loop=True
   
    if animalCode=='quit':
        check=True
        break
   
    if(len(animalCode.split()))>3:

        if animalCode!='print' and animalCode!='quit' and animalCode.split()[0]!='log' and animalCode!='':
            print('>Could not interpret command.')
            check=True

        if animalCode.split()[0]=='log':
            count+=1
            check=True

            if (animalCode.split()[1] in log)==True:
                if animalCode.split()[2].isalpha() and animalCode.split()[3].isalpha():
                    print(">The ordinates should be integers.")
                    print('Commands: print, log <animal id> <x ord> <y ord>, quit.')

                else:
                    if type(eval(animalCode.split()[2]))==int and type(eval(animalCode.split()[3]))==int:
                        log[animalCode.split()[1]]=str(animalCode.split()[2])+'#'+str(animalCode.split()[3])
                        sign='>'

                    else:
                        print(">The ordinates should be integers.")
                        print('Commands: print, log <animal id> <x ord> <y ord>, quit.')
                    
            else:
                print('>That animal identity code is unknown.')
                
    if animalCode=='print':
        sign=''
        check=True
        j=0

        for i in log:
            if log[i]=="":
                if j==0:
                    print(str(count*'>')+'Animal',i+' cannot be located.')
                else:
                    print('Animal',i+' cannot be located.') 
            else:
                if j==0:
                    print(str(count*'>')+'Animal',i,'last seen at','('+log[i].split('#')[0]+', '+log[i].split('#')[1]+').')
                else:
                    print('Animal',i,'last seen at','('+log[i].split('#')[0]+', '+log[i].split('#')[1]+').')
            j+=1

    if check==False and animalCode!='':
        print('>Could not interpret command.')
        print('Commands: print, log <animal id> <x ord> <y ord>, quit.')

    n=animalCode=input()
        
print('>'+sign)
