import random
num = random.randint(1,100)
guess=int(input("guess number: "))
i=0
while num != guess:
	if i>3:
		print("game over!")
		break			
	if num > guess:
		print("too high!")
	else:
		print("too low!")
	i+=1
	guess = int(input("guess number: "))
		
			
else:
	print("exactly right!")	
