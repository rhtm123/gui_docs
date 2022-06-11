## import 
import PySimpleGUI as sg
## layout
layout = [
    [sg.InputText(default_text="",size=(20,2), key="input")],
    [sg.Button("7",size=(4,2),key="7"), sg.Button("8",size=(4,2),key="8"), sg.Button("9",size=(4,2),key="9"), sg.Button("/",size=(4,2),key="/")],
    [sg.Button("4",size=(4,2),key="4"), sg.Button("5",size=(4,2),key="5"), sg.Button("6",size=(4,2),key="6"), sg.Button("*",size=(4,2),key="*")],
    [sg.Button("1",size=(4,2),key="1"), sg.Button("2",size=(4,2),key="2"), sg.Button("3",size=(4,2),key="3"), sg.Button("-",size=(4,2),key="-")],
    [sg.Button("0",size=(4,2),key="0"), sg.Button(".",size=(4,2),key="."), sg.Button("=",size=(4,2),key="equal"), sg.Button("+",size=(4,2),key="+")],
]

### window 
window = sg.Window("Calculator",layout=layout,resizable=True,font=("calibri",24))

## 
def update(event):
    input_elem = window["input"]
    current_value = input_elem.get()
    input_elem.update(current_value+event)

def calculate(event):
    input_elem = window["input"]
    current_value = input_elem.get()
    try:
        ans = eval(current_value)
        input_elem.update(ans)
    except:
        input_elem.update("")


## event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        # print("window closed")
        break
    if event in "1234567890.+-*/":
        update(event)

    if event == "equal":
        calculate(event)

## window close
window.close()