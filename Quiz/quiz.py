import tkinter as tk
from tkinter import messagebox
import csv
import tkinter.font as font

window = tk.Tk()
window.columnconfigure(0, minsize=400, weight=1)
window.rowconfigure([0, 1], minsize=240, weight=1)
window.configure()
window.title("Quiz")
count = 0
score = 0

question_font = font.Font(family='Impact', size=18)
option_font = font.Font(family='Impact', size=13)

questions = []


def get_ques():
    global count
    global questions
    with open('Quiz/quiz_questions.csv') as f:
        quiz = csv.reader(f, delimiter=',')
        column_count = 0
        for i in quiz:
            if column_count != 0:
                questions.append(i)
            column_count += 1

    return questions[count]


get_ques()

question_number = len(questions)-1


def check_answer(chosen, correct):
    global score
    global count
    if chosen == correct:
        score += 1

        print(score)
    else:
        print(score)

    if(count != question_number):
        count += 1
    else:
        messagebox.showinfo(
            title='Score', message=f'Your Final score is {score}')
        window.destroy()
    question_label.configure(text=f'{count+1}.{questions[count][0]}:')
    option_a.configure(text=f'{questions[count][1]}')
    option_b.configure(text=f'{questions[count][2]}')
    option_c.configure(text=f'{questions[count][3]}')
    option_d.configure(text=f'{questions[count][4]}')


# Setup Frames

# Question Box Frame Setup:
question_frame = tk.Frame(master=window)
question_frame.rowconfigure(0, minsize=120)
question_frame.columnconfigure(0, minsize=400)
question_frame.grid(row=0, column=0)

# Answers Option Frame Setup:
answers_frame = tk.Frame(master=window)
answers_frame.grid(row=1, column=0)
answers_frame.rowconfigure(0, minsize=120, weight=1)
answers_frame.columnconfigure(0, minsize=400, weight=1)

# Question Setup


question_label = tk.Label(
    master=question_frame, text=f'{count+1}.{questions[count][0]}:', font=question_font)
question_label.grid()
option_a = tk.Button(master=answers_frame, text=f'{questions[count][1]}',
                     height=10, width=56, relief='raised', font=option_font, bg='#84FFC9')

option_a.grid(row=0, column=0, sticky='w')
option_b = tk.Button(master=answers_frame, text=f'{questions[count][2]}',
                     height=10, width=56, relief='raised', font=option_font, bg='#8AF2D2')
option_b.grid(row=0, column=1, sticky='e')
option_c = tk.Button(master=answers_frame, text=f'{questions[count][3]}',
                     height=10, width=56, relief='raised', font=option_font, bg='#91E5DB')
option_c.grid(row=1, column=0, sticky='w')
option_d = tk.Button(master=answers_frame, text=f'{questions[count][4]}',
                     height=10, width=56, relief='raised', font=option_font, bg='#97D9E4')
option_d.grid(row=1, column=1, sticky='e')

option_a.configure(command=lambda: check_answer(
    option_a.cget('text'), questions[count][5]))
option_b.configure(command=lambda: check_answer(
    option_b.cget('text'), questions[count][5]))
option_c.configure(command=lambda: check_answer(
    option_c.cget('text'), questions[count][5]))
option_d.configure(command=lambda: check_answer(
    option_d.cget('text'), questions[count][5]))

window.mainloop()
