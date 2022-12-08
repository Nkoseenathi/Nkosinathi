.text
.globl main

main:
la $a0, number
li $v0, 4 
syscall 

li $v0, 5 
syscall 
move $t5, $v0
 
la $a0, output
li $v0, 4 
syscall 

li $t1,9
li $t2,2
li $t3,0


loop: 
	addi $t0,$t5,0
	div  $t0,$t2
	mfhi $t3
	
	bne $t3,0,else

		move $a0, $t2 
		li $v0, 1 
		syscall 
		
		la $a0, line 
		li $v0, 4 
		syscall 
		
		j exit
		
	else:
		addi $t3,$t3,0
	exit:
	
	bne $t2,$t1,stop
		li $v0, 10 
		syscall 
	stop:
		addi $t2,$t2,1
		j loop

# Data for the program:
.data
number: .asciiz "Enter a number:\n"
output: .asciiz "The single digit divisors are:\n"
line: .asciiz "\n"