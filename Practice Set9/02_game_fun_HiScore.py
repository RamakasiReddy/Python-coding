import random

def game():
    print("game running...")
    you = random.randint(1,100)
    with open("021_HiScore.txt") as f:
        hiscore = f.read()
        if(hiscore !=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

        print(f"your score is {you}")
    if(you>hiscore):
        with open("021_HiScore.txt","w") as f:
            f.write(str(you))
            print("you have just broken the high score")
        # return you
game()
        