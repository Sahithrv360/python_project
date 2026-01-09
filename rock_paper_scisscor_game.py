import random
from tabulate  import tabulate 
move = {1 : 'rock',2 : 'paper',3 : 'scissor'}
is_playing = True
points = {'player_points' : 0,'computer_points':0}
pp,cp = 0,0

while is_playing:
    computer_move = random.choice(list(move.values()))
    your_move = input('Enter your move (rock,paper,scissor,q:Quit) : ')
    if your_move in list(move.values()):
        try:
            print(computer_move)
            if computer_move ==  'rock' and your_move == 'paper':
                print('You win,will u continue')
                pp += 1
                points['player_points'] = pp
            
            elif computer_move ==  'paper' and your_move == 'scissor':
                print('You win,will u continue')
                pp += 1
                points['player_points'] = pp
                
            elif computer_move ==  'scissor' and your_move == 'rock':
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
        if your_move.lower() == 'q':
            break
        print('Enter a valid value')

table = [[key,value] for key,value in points.items()]
print(tabulate(table,headers=['player_name','points'],tablefmt="grid"))
