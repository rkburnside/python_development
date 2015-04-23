#-------------------------------------------------------------------------------
# Name:        Amateur Radio Test
# Purpose:
#
# Author:      Richard
#
# Created:     27/12/2011
# Copyright:   (c) Richard 2011
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    pass

if __name__ == '__main__':
    main()

import easy_gui_test as eg
import random

T0A = 0 + random.randint(0,12)
T0B = 13 + random.randint(0,10)
T0C = 24 + random.randint(0,10)
T1A = 35 + random.randint(0,10)
T1B = 46 + random.randint(0,10)
T1C = 57 + random.randint(0,10)
T1D = 68 + random.randint(0,10)
T1E = 79 + random.randint(0,10)
T1F = 90 + random.randint(0,12)
T2A = 103 + random.randint(0,10)
T2B = 114 + random.randint(0,10)
T2C = 125 + random.randint(0,8)
T3A = 134 + random.randint(0,10)
T3B = 145 + random.randint(0,10)
T3C = 156 + random.randint(0,10)
T4A = 167 + random.randint(0,10)
T4B = 178 + random.randint(0,10)
T5A = 189 + random.randint(0,10)
T5B = 200 + random.randint(0,10)
T5C = 211 + random.randint(0,10)
T5D = 222 + random.randint(0,11)
T6A = 234 + random.randint(0,10)
T6B = 245 + random.randint(0,11)
T6C = 257 + random.randint(0,12)
T6D = 270 + random.randint(0,10)
T7A = 281 + random.randint(0,12)
T7B = 294 + random.randint(0,11)
T7C = 306 + random.randint(0,10)
T7D = 317 + random.randint(0,10)
T8A = 328 + random.randint(0,10)
T8B = 339 + random.randint(0,10)
T8C = 350 + random.randint(0,10)
T8D = 361 + random.randint(0,10)
T9A = 372 + random.randint(0,10)
T9B = 383 + random.randint(0,10)


sections = [T0A,T0B,T0C,T1A,T1B,T1C,T1D,T1E,T1F,T2A,T2B,T2C,T3A,T3B,T3C,T4A,T4B,T5A,T5B,T5C,T5D,T6A,T6B,T6C,T6D,T7A,T7B,T7C,T7D,T8A,T8B,T8C,T8D,T9A,T9B]

line = open('Test.txt', 'r')

##Seciton*Question #*Answer*Question*A*B*C*D
question = line.readlines()
total = 0.0
percentage = 0.0

for line_num in range(35):
    question_line = question[sections[line_num]]
    question_line = question_line.split('*')
    msg = 'Question #' + str(line_num+1) + ' - ' + question_line[1] + '\n\n' + question_line[3]
    title = question_line[0]
    choices = [question_line[4],question_line[5],question_line[6],question_line[7]]
    choice = eg.choicebox(msg, title, choices)
    choice = choice.split('. ')

    answer = 0
    if question_line[2] == 'A':
        answer = question_line[4]
    elif question_line[2] == 'B':
        answer = question_line[5]
    elif question_line[2] == 'C':
        answer = question_line[6]
    elif question_line[2] == 'D':
        answer = question_line[7]

    if choice[0] == question_line[2]:
        total = total + 1
        percentage = total / (line_num + 1)
        eg.msgbox(msg='Correct\n\n' + 'Question - ' + question_line[1] + '\n' + question_line[3] + '\n\nAnswer\n' + answer + '\n\nTotal Correct: {} / '.format(int(total)) + str(line_num+1) + '\t\tPercentage Correct: {:.1%}'.format(percentage), title='', ok_button='OK')
    else:
        percentage = total / (line_num + 1)
        eg.msgbox(msg='Wrong!!!\n\n' + 'Question - ' + question_line[1] + '\n' + question_line[3] + '\n\nAnswer\n' + answer + '\n\nTotal Correct: {} / '.format(int(total)) + str(line_num+1) + '\t\tPercentage Correct: {:.1%}'.format(percentage), title='', ok_button='OK')

line.close()

if total >= 26.0:
    eg.msgbox('You answered {} questions correctly for {:.1%} score.'.format(int(total),percentage) + '\n\nYou Passed. Congrats!')
else:
    eg.msgbox('You answered {} questions correctly for {:.1%} score.'.format(int(total),percentage) + '\n\nYou are a complete failure.')