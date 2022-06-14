# Write your code here
import random

def pick_options(option_list, option):
    index = option_list.index(option)
    win_list = option_list[index + 1:]
    lose_list = option_list[:index]
    if len(win_list) < len(lose_list):
        diff = len(lose_list) - len(win_list)
        for i in range(diff - diff % 2):
            win_list.append(lose_list.pop(i))
            break
    elif len(lose_list) < len(win_list):
        diff = len(win_list) - len(lose_list)
        for i in range(diff - diff % 2):
            lose_list.append(win_list.pop(-(i + 1)))
            break

    # print(win_list)
    # print(lose_list)
    return win_list, lose_list


variants = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
input_options = [['rock', 'paper', 'scissors'], '!exit', '!rating']
play_options = ['rock', 'paper', 'scissors']
user_name = input('Enter your name:')
user_score = 0
print('Hello,', user_name)
with open('rating.txt', 'r') as scores:
    for line in scores:
        if user_name in line:
            user_score += int(line.split()[-1])
user_options = input().split(',')
if user_options != ['']:
    play_options = user_options
print("Okay, let's start")
user_play = 'random'
while user_play != '!exit':
    user_play = input()
    if user_play == '!rating':
        print('Your rating:', user_score)
        continue
    elif user_play == '!exit':
        break
    elif user_play not in play_options:
        print('Invalid input')
        continue
    ai_play = random.choice(input_options[0])
    win, lose = pick_options(play_options, user_play)


    if ai_play == user_play:
        print(f'There is a draw ({ai_play})')
        user_score += 50
        continue
    elif ai_play in win:
        print(f'Sorry, but the computer chose {ai_play}')
        continue
    elif ai_play in lose:
        print(f'Well done. The computer chose {ai_play} and failed')
        user_score += 100
        continue
print('Bye!')
