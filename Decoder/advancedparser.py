id_number=input('Please enter your ID number:\n')
_sum=0

for i in range(13,1,-1):

    if i%2==0:
        _sum+=(int(id_number[-i])*2)%9

    else:
        _sum+=int(id_number[-i])
        
if (10-_sum%10)==int(id_number[-1]):

    date_of_birth=id_number[4:6]+'/'+id_number[2:4]+'/'+id_number[0:2]
    gender=''
    sex=id_number[6:10]

    if 5000<=int(sex)<=9999:
        gender='male'

    elif 0000<=int(sex)<=4999:
        gender='female'

    else:
        gender='Other'

    citezenship_check=int(id_number[10])

    if citezenship_check==0:
        citezenship='South African citizen'

    else:
        citezenship='permanent resident'
        
    print('Your date of birth is',date_of_birth+'.')
    print('You are',gender+'.')
    print('You are a',citezenship+'.' )   
 
else:
    print('Invalid ID number.')
    
    
        
    
