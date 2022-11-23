import PySimpleGUI as sg
layout = [[sg.Text('Enter Your Passcode')],
[sg.Input(size=(30, 1), justification='left', key='input')],
[sg.Button('1'), sg.Button('2'), sg.Button('3')],
[sg.Button('4'), sg.Button('5'), sg.Button('6')],
[sg.Button('7'), sg.Button('8'), sg.Button('9')],
[sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')],
[sg.Text("No binary numbers",size=(15, 1), font=('Helvetica', 18), text_color='white', key='out')]]
window = sg.Window('Keypad', layout, default_button_element_size=(5,2), auto_size_buttons=False)
def decToBin(decNum):
    decNum = int(decNum)
    binNum = ''
    while decNum > 0:
        binNum = str(decNum % 2) + binNum
        decNum = decNum // 2
    return str(binNum)
keys= ''
binNum = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Clear':
        keys= ''
        window['out'].update("No binary numbers")
    elif event in '1234567890':
        keys = values['input']
        keys += event
    elif event == 'Submit':
        binNum = decToBin(keys)
        window['out'].update(binNum) # вивести повідомлення "ВІДКРИТО"
    window['input'].update(keys)
