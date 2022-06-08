
## import 
import PySimpleGUI as sg

## theme 

## layout

current = "X"

win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
## check if current wins the game -> True or False 
def check_win():
    for i in win_comb:
        f, s, t = i[0],i[1],i[2]
        b1 = window[f]
        b2 = window[s]
        b3 = window[t]
        v1 = b1.get_text()
        v2 = b2.get_text()
        v3 = b3.get_text()
        # print(v1,v2,v3)
        if (v1==current and v2==current and v3==current):
            return True
    return False


def change_text(event):
    global current
    window[event].update(current)
    if check_win():
        return True
    current = "X" if current=="O" else "O"
    return False


layout = [
    [sg.Button("", key=1, size=(4,2), pad=10), sg.Button("",key=2, size=(4,2), pad=10), sg.Button("", key=3, size=(4,2), pad=10)],
    [sg.Button("", key=4, size=(4,2), pad=10), sg.Button("",key=5, size=(4,2), pad=10), sg.Button("", key=6, size=(4,2), pad=10)],
    [sg.Button("", key=7, size=(4,2), pad=10), sg.Button("",key=8, size=(4,2), pad=10), sg.Button("",key=9, size=(4,2), pad=10)],
]

window = sg.Window("Tic Tac Toe", layout=layout, resizable=True)

while True:
    event, values = window.read()
    if event == "-close-" or event== sg.WIN_CLOSED:
        break
    if event:
        win = change_text(event)
        if (win):
            sg.Popup(f"{current} wins the game")
            break
        

window.close()