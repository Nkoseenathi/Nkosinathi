gmv=eval(input('What is the gross vehicle mass (in kg)?\n'))
v_class=''
gmv_trailer=0

if gmv<=3500:
    v_class='B'

elif 3500<=gmv<=16000:
    v_class='C1'

elif gmv>16000:
    v_class='C'

trailer=input('Does the vehicle have a trailer?\n')

if trailer=='y':
    gmv_trailer=eval(input('What is gross vehicle mass of the trailer (in kg)?\n'))
    if gmv_trailer>750:
        v_class='E'+v_class 
else:
    articulated=input('Is the vehicle articulated?\n')
    if articulated=='y':
        v_class='E'+v_class    

print('This vehicle is class',v_class+'.')


