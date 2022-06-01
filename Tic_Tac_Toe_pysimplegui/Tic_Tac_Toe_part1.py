
## Import
import PySimpleGUI as sg

## theme
sg.theme("Dark")

## layout

layout = [
    [sg.Text("Hello World"), sg.Input("")],
    [sg.Button("Ok", key="-ok-"), sg.Button("Close",key="-close-")],
    [sg.Button("click")]
]

## window

window = sg.Window("TIC TAC TOE", layout=layout, resizable=True)

## event loop
while True:
    event, values = window.read()
    if event == "-close-" or event== sg.WIN_CLOSED:
        break
    if event == "-ok-":
        print(values)

## close the window
window.close()