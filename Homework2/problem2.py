import random
num = random.randint(1,100)
print(num)
guess=input("guess number: ")
i=0
if (guess) == "exit":
	print("exit !")	
else:
	while num != int(guess):	
		if i>3:
			print("game over!")
			break			
		if num > int(guess):
			print("too high!")
		else:
			print("too low!")
		i+=1
		guess = input("guess number: ")	
		if (guess) == "exit":
			print("exit !")	
			break			
	else:
		print("exactly right!")	
