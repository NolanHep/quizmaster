import os, random, time, re
r = random.SystemRandom()
score = 0
def start():
    try:
        open("Saves.csv", "x"), open("Highscores.txt", "x")
    except FileExistsError:
        return 'files_exist'

def character_info(score):
    print('Welcome to the quiz!')
    time.sleep(1)
    print('I am your host Nolsters TV')
    print('')
    print('What is your name?')
    name = input('>>>')
    f = open("saves.txt", "r+")
    line = f.readlines()
    if name in line[0].strip():
        score = line[1]
    else:
        f = open("Saves.csv", "a")
        f.write(name+"\n")
    return score

def question(score):
    f = open("Questions.txt", "r")
    line = f.readlines()
    r = open("saves.txt", "r+")
    if score != 0:
        score_1 = int(r.readline(1))
        score_2 = int(r.readline(2))
        score = score_1 + score_2
    else:
        game = 0
        while game == 0:
            number_lines = sum(1 for line in open("questions.txt"))
            odd_lines = list((i for i in range(1, number_lines) if i % 2 != 0))
            choice = random.choice(odd_lines)
            choice = choice - 1
            print(line[choice])
            answer = input('>>>')
            if answer.title() == line[choice + 1].strip() and score < 10:
                score = score + 1
                print('correct', score)
            elif answer != 'save' and score < 10:
                print('wrong', score)
            elif answer == 'save':
                save = open("Saves.csv", "a")
                score = str(score)
                save.write(score)
                print('Nolan that was a great score of', score+', we saved it for you if you want to return!')
                game = 1
            elif score >= 10:
                print('Good game your score is', score)
                game = 1
        print('And we are back?')

start()
character_info(score)
question(score)