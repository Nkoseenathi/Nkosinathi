
main:
	li $t6,2
    li $t7,9
	la $a0, one_msg
	li $v0, 4 
	syscall

	li $v0, 5 
	syscall 
	move $t0, $v0
	
	la $a0, two_msg
	li $v0, 4 
	syscall

	li $v0, 5 
	syscall 
	move $t1, $v0 
	
loop:

	div $t3,$t0,$t6
	mfhi $t2
	
	div $t5,$t1,$t6
	mfhi $t4
	
	
	bne $t2,0,incr
		add $t8,$t8,1
		j exit
		
	bne $t4,0,incr
		add $t8,$t8,1
		j exit
	incr:
		add $t8,$t8,0
	
	exit:
			
	beq $t6,$t7,endloop

	addi $t6,$t6,1
		
	j loop
	
endloop:
		bne $t8,0,then
	
		la $a0, prime_msg
		li $v0, 4 
		syscall
		
		li $v0, 10 
		syscall
		j exit
		then: 
	
		la $a0, notPrime_msg
		li $v0, 4 
		syscall

		li $v0, 10 
		syscall

	
	
	
	
	
	
.data
one_msg: .asciiz "Enter the first number:\n"
two_msg: .asciiz "Enter the second number:\n"
notPrime_msg: .asciiz "The two numbers are not relatively prime\n"
prime_msg: .asciiz "The two numbers are relatively prime\n"