import random

score = 0
def play(rounds):
    for i in range(rounds):

        user = input("'r for rock', 'p for paper' , 's for scissors' = ")
        computer = random.choice(['r','p','s'])

        if user == computer:
            print("Its tie")
            global score
            score=score+1
        elif is_win(user,computer):
            print("you win")
        else:
            print("you lost")

    if score > rounds/2+1:
        print(f"\n*** you won the round with {score} points ***")
    else :
        print(f"\n*** you lost the round by {rounds-score} points ***")

def is_win(player , opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or \
       (player=='s' and opponent=='p'):
       global score
       score=score+1
       return True

rounds = int(input("how many rounds to play : "))
play(rounds)