main:
li $t6,5
li $t5,1
loop:
	la $a0, number
	li $v0, 4 
	syscall

	li $v0, 5 
	syscall 
	move $t0, $v0
	
	div $t1,$t0,2
	mfhi $t2
	
	div $t3,$t0,3
	mfhi $t4

		add $t7,$t4,$t2
		bne $t7,0,else
		la $a0, output
		li $v0, 4 
		syscall	
		j exit
	else:
	
		bne $t2,0,three
		la $a0, two_msg
		li $v0, 4 
		syscall	
		j exit
		
		three:
		
			bne $t4,0,nun
			la $a0, three_msg
			li $v0, 4 
			syscall	
			j exit
		
		nun:
					
			la $a0, none_msg
			li $v0, 4 
			syscall	
		exit:
	
	
	bne $t6,$t5,stop
		li $v0, 10 
		syscall 
	stop:
		addi $t5,$t5,1
		
	j loop
			

# Data for the program:
.data
number: .asciiz "Enter a number:"
two_msg: .asciiz "It is divisible by 2\n"
three_msg: .asciiz "It is divisible by 3\n"
output: .asciiz "It is divisible by both 2 and 3\n"
none_msg: .asciiz "It is neither divisible by 2 nor 3\n"

line: .asciiz "\n"