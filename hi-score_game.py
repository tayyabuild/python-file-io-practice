'''The game() function in a program lets a user play a game and returns the score as an
integer. You need to read a file ‘Hi-score.txtʼ which is either blank or contains the previous
Hi-score. You need to write a program to update the Hi-score whenever the game()
function breaks the Hi-score.'''


import random                                  #imports the random library to this program

def game():                                    # defines the function 'game'
    print("You're playing a game...")

    '''the line of code given BELOW, uses the random library to generate a random number between '1' and '62' every time the program runs. 
    And stores the value in the varible 'score' '''   
    score = random.randint(1, 62)  
 
    with open("hi_score.txt") as f:            # opens the file in read mode (by deafult)
        hiscore = f.read().strip()             # the strip function removes all the whitespaces(if any) from the file 'hi_score.txt'
        if hiscore != "":                      # if there is already a hiscore (the file's not empty), then its converted into an integer
            hiscore = int(hiscore)
        else:                                  # if the file is empty, the hiscore is set to zero by default
            hiscore = 0
        print(f"Your score: {score}")

        '''in the block of code BELOW, if your score in the current round is greater then the high score, the file 'hi_score.txt' is 
        opened in write mode and the hicore is replaced with your current score (your score becomes the new hiscore)'''

        if score > hiscore:        
            with open("hi_score.txt", "w") as f:
                f.write(str(score))

        return score






game()


