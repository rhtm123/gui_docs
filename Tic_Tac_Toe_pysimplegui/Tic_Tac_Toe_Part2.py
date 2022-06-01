
## import 
import PySimpleGUI as sg

## theme 

## layout

current = "X"

def change_text(event):
    global current
    # print(event)
    window[event].update(current)
    # if current = "X":
    #     current = "O"
    # else:
    #     current = "X"
    u = window[event]
    # print(u.get_text())
    current = "X" if current=="O" else "O"


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
        change_text(event)
        

window.close()