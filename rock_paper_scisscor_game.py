import random
from tabulate  import tabulate

move = {1 : 'rock',2 : 'paper',3 : 'scissor'}
#is_playing = True
points = {'player_points' : 0,'computer_points':0}
pp,cp = 0,0

while True:
    computer = random.choice(list(move.values()))
    player = input('Enter your move (rock,paper,scissor,q:Quit) : ')
    if player in list(move.values()):
        try:
            print(f'Computer :{computer:^}')
            print(f'Player   :{player:^}')
            if computer == player :
                print('Its a tie ...')
            elif computer ==  'rock' and player == 'paper':
                print('You win,will u continue')
                pp += 1
                points['player_points'] = pp
            
            elif computer ==  'paper' and player == 'scissor':
                print('You win,will u continue')
                pp += 1
                points['player_points'] = pp
                
            elif computer ==  'scissor' and player == 'rock':
                print('You win,will u continue')
                pp += 1
                points['player_points'] = pp
                
            else :
                print('You loose,will u continue')
                cp += 1
                points['computer_points'] = cp
                
        except Exception:
            pass
    else :
        if player.lower() == 'q':
            break
        print('Enter a valid value')

table = [[key,value] for key,value in points.items()]
print(tabulate(table,headers=['Name','Points'],tablefmt="grid"))
