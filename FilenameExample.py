import PySimpleGUI as sg

def save_previous_filename_demo():

    # Notice that the Input element has a default value given (first parameter) that is read from the user settings
    layout = [[sg.Text('Enter a filename:')],
              [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()],
              [sg.B('Save'), sg.B('Exit Without Saving', key='Exit'), sg.T('(or click X to close without saving)')]]

    window = sg.Window('Luu Tien Phat', layout)

    while True:
        event, values = window.read()
        if event in (sg.WINDOW_CLOSED, 'Exit'):
            break
        elif event == 'Save':
            sg.user_settings_set_entry('-filename-', values['-IN-'])

    window.close()


if __name__ == '__main__':
    sg.user_settings_filename(path='.')  # Set the location for the settings file
    # Run a couple of demo windows
    save_previous_filename_demo()