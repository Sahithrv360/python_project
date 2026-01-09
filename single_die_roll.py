import random

''' ● ┌ ─ ┐ │ └ ┘ '''
''' \u25CF '''
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

while roll_die:
    player = input('Do you want to roll the die (y/n) : ')
    if player.lower() == 'y':
        number = random.choice(roll)
        for val in number:
            print(val)
    elif player.lower() == 'n':
        print('Thank you for using the die')
        roll_die = False
    else :
        print('Enter either y/n !!!')
