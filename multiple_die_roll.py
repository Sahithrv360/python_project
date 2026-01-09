import random

''' ● ┌ ─ ┐ │ └ ┘ '''
'''Ascii codes for above symbols : \u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518 '''

roll = ( ('┌─────────┐',
          '│         │',
          '│    ●    │',
          '│         │',
          '└─────────┘' ),
         ('┌─────────┐',
          '│ ●       │',
          '│         │',
          '│       ● │',
          '└─────────┘' ),
         ('┌─────────┐',
          '│ ●       │',
          '│    ●    │',
          '│       ● │',
          '└─────────┘' ),
         ('┌─────────┐',
          '│ ●     ● │',
          '│         │',
          '│ ●     ● │',
          '└─────────┘' ),
         ('┌─────────┐',
          '│ ●     ● │',
          '│    ●    │',
          '│ ●     ● │',
          '└─────────┘' ),
         ('┌─────────┐',
          '│ ●     ● │',
          '│ ●     ● │',
          '│ ●     ● │',
          '└─────────┘' ) )

roll_die = True
number_of_dice = int(input('Number of dices do you want to roll at a time : '))
while roll_die:
    player = input('Do you want to roll the dice (y/n) : ')
    if player.lower() == 'y':
        for _ in range(number_of_dice):
            number = random.choice(roll)
            for val in number:
                print(val)
    elif player.lower() == 'n':
        print('Thank you for using the dice')
        roll_die = False
    else :
        print('Enter either y/n !!!')
