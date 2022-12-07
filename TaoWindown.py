import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Nội dung hiển thị:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Hiển thị'), sg.Button('Thoát')]]

window = sg.Window('Luu Tien Phat', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Thoát':
        break
    if event == 'Hiển thị':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()