from PySimpleGUI import PySimpleGUI as sg

class Interface:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Usuário:  ',size=(26,0)),sg.Input(key=('usuario'))],
            [sg.Text('Senha:    'size=(26,0)),sg.Input(key=('senha'))],
            [sg.Text('Usuário de referência:    ',size=(26,0)),sg.Input(key=('usuario_referencia'))],
            [sg.Output(size=(60,15))]
            [sg.Button('Iniciar')]
        ]
        