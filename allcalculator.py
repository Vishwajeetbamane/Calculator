#Author: Vishwajeet Bamane
#Modified Date: 1 May 2020

var9 = 1
while var9 == 1:
	print("........Welcome to the Calculator........")
	print("+ for Add\n- for Subtraction\n* for Multiply\n/ for Divide\n")




	print("Press Enter to run again")
	print("Choose a operator from above:")
	var1=input()

#For Addition
	if var1 == "+":
		add1 = input("Enter your first number:\n")
		add2 = input("Enter your second number:\n") 
		addresult = int(add1) + int(add2)
		print("Sum of" , add1 ,"and", add2, "is equal to", addresult)
		print("Thank you!")
		var8 = input()
#For Subtraction
	if var1== "-":
		sub1 = input("Enter the number you want to subtract from:\n")
		sub2 = input("Enter the number you want to subtract\n")
		subresult = int(sub1) - int(sub2)
		print(sub2, "subtracted from", sub1,"is equal to", subresult )
		print("Thank you!")
		var8 = input()
#For Multiplication
	if var1== "*":
		mul1 = input("Enter the first number:\n")
		mul2 = input("Enter the second number:\n")
		mulresult = int(mul1) * int(mul2)
		print("Multiplication of" ,mul1 ,"and" ,mul2, "is equal to", mulresult )
		print("Thank you!")
		var8 = input()
	#For Division
	if var1== "/":
		div1 = input("Enter the dividend:\n")
		div2 = input("Enter the divisor:\n")
		divresult = int(div1) / int(div2)
		print(div1, "divided by", div2, "is equal to", divresult)
		print("Thank you!")
		var8 = input()

	if var1 == "Q":
		break
