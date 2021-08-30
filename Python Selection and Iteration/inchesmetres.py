inches=eval(input('Enter the minimum number of inches (not less than 0):\n'))
max_inches=eval(input('Enter the maximum number of inches (not greater than 11):\n'))

print('Inches:',end='')

for i in range(inches,max_inches+1):
    metres=round((i/12)/3.28084,2)
    print("{:>5}".format(i),end='')

print('\nMetres:',end='')

for i in range(inches,max_inches+1):
    metres=((i/12)/3.28084)
    print("{:>5.2f}".format(metres),end='')

