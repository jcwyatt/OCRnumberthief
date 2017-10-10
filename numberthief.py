'''Thief!
A thief has managed to find out the four digits for an online PIN code, 
but doesn’t know the correct sequence needed to hack into the account.
Design and write a program that displays all the possible combinations 
for any four numerical digits entered by the user. The program should avoid 
displaying the same combination more than once.
Submit a fully detailed Showcase for your program.'''

from random import shuffle

fourDigits = input("What are the secret digits? : ")

while not fourDigits.isnumeric() or len(fourDigits)!=4:
	fourDigits = input("They are not four numbers. Enter more carefully please. : ")

#badway:
digit=[]
for num in fourDigits: 
	digit.append(num)

print ("%s%s%s%s" %(digit[0],digit[1],digit[2],digit[3]))


combiStore=[]
for i in range(0,100):
	shuffle(digit)
	newOrder="%s%s%s%s" %(digit[0],digit[1],digit[2],digit[3])
	if newOrder not in combiStore:
		print (newOrder)
		combiStore.append(newOrder)
	else:
		print("duplicate",i)
	if len(combiStore)==24:
		break

print(len(combiStore))
print (combiStore)



