import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number,highest_number)
guesses = 0

is_palying = True

while is_palying :
    
    guess = input('Enter the number : ')
    guesses += 1
    if guess.isdigit() :
        guess = int(guess)
        if guess < lowest_number or guess > highest_number:
            print('Invalid number')
            print(f'The guess should be in range of {lowest_number} and {highest_number}')
        else:
            if guess > answer :
                print('Invalid guess')
                print('The guess is too high')
            
            elif guess < answer :
                print('Invalid guess')
                print('The guess is too low')
            
            else :
                print('You guessed it correctly')
                print(f'Number of guesses : {guesses}')
                break
                is_playing = False
    else :
        print('Invalid Value')
        print(f'The guess should be in range of {lowest_number} and {highest_number}')
    
