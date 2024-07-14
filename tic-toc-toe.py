from tkinter import *
import random

import row


def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:  # Player's move
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
                window.after(500, computer_move)
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

def computer_move():
    global player
    if check_winner() is False:
        row, column = random.choice(empty_spaces())
        buttons[row][column]['text'] = player
        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0] + " turn"))
        elif check_winner() is True:
            label.config(text=(players[1] + " wins"))
        elif check_winner() == "Tie":
            label.config(text="Tie!")

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row]2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0].config(bg="green")
            buttons[1].config(bg="green")
            buttons[2].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = [(row, column) for row in range(3) for column in range(3) if buttons[row][column]['text'] == ""]
    return spaces

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
    if player == players[1]:
        window.after(500, computer_move)

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
        command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

if player == players[1]:
    window.after(500, computer_move)

window.mainloop()