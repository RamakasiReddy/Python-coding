import random
'''1 for snake
   -1 for water
   0 for gun'''

computer = random.choice([-1,0,1])
youstr = input("Enter your Choice")
playerDict = {"snake":1 ,"water":-1,"gun":0}
rev = {1 : "Snake", -1 : "Water",0 :"Gun"}


you = playerDict[youstr]
print(f"{rev[you]}\n{rev[computer]}")

if(computer == you):
    print("both draw")
elif(you == 1 and computer == 0 ):
    print("you loose")
elif(you == -1 and computer == 0):
    print("you win")
elif(you == 0 and computer == 1 ):
    print("you win ")
elif(you == 0 and computer == -1):
    print("you win")
elif(you == 1 and computer == -1 ):
    print("you win")
elif(you == 1 and computer == 0):
    print("you loose")
else:
     print("something went wrong")



