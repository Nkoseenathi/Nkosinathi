feet=eval(input('Enter the minimum number of feet (not less than 0):\n'))
max_feet=eval(input('Enter the maximum number of feet (not more than 99):\n'))
metres=0

for i in range(feet,max_feet+1):
    metres=i/3.28084
    print("{:>4}".format(str(i))+"'"+' |   '+"{:0>2.2f}".format(metres)+'m')
