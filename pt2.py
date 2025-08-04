#  the game () function in program let   a s user play a game and return the score as ab integer you need to read a file 'hi-score ' which is either blank or  contains the priovous hi score you need to write a program to update the hi-score whentever the game  funtion break the hi score

import random

def game():
    print("You are playing the game.")

    score = random.randint(1, 62)
    # fetch the hiscore
    with open("file-input-output/hiscore.txt") as f:
        hiscore = f.read().strip()  
        
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score:{score}")
    
    if score > hiscore:
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

      
    return score
game()
