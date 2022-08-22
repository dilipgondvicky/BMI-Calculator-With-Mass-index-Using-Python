def bmicalculate(height, weight):
	height = height/100
	bmi=weight/(height**2)
	print("Your Body Mass Index Is: ",bmi)
	if(bmi>0):
		if(bmi<=16):
			print("you are severely underweight")
		elif(bmi<=18.5):
			print("you are underweight")
		elif(bmi<=25):
			print("you are healthy and normal")
		elif(bmi<=30):
			print("you are overweight")
		elif(bmi<=35):
			print("you are moderately obese")
		else: print("you are severely obese")
	else:("enter valid details")	
while True:
	height1=float(input("Enter Your Height In Centimeters: "))
	weight1=float(input("Enter Your Weight In K.G: "))
	bmicalculate(height1, weight1)
	a = input('Type yes to Continue \n Type Somenthing To Exit \n') 
	if a == 'yes':
		continue
	else:
		break
