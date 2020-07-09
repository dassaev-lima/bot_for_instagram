import PySimpleGUI as sg
from insta_bot import InstaBot
from time import sleep


class Interface:
    #para a criação de uma interface é preciso ter ter parametros base
    def __init__(self):
        #mudar o estilo de cores da janela
        sg.theme('DarkAmber')
        #layout
        layout = [
            [sg.Text('Usuário:  ',size=(10,0),text_color=('white')),
                sg.Input(size=(20,0),key=('usuario'),text_color=('white'))
            ],
            [sg.Text('Senha:',size=(10,0),text_color=('white')),
                sg.Input(size=(20,0),key=('senha'),text_color=('white'))
            ],
            [sg.Text('Usuário de referência:',size=(10,0),text_color=('white')),
                sg.Input(size=(20,0),key=('usuario_referencia'),text_color=('white'))
            ],
            [sg.Button('Iniciar')],
            [sg.Output(size=(60,15))]
        ]
        #janela
        self.janela = sg.Window('Siga mais usuários em menos tempo').layout(layout)
        
    
    def iniciar(self):
        while True:
            #extrair os dados da tela
            self.button,self.values = self.janela.Read()
            
            usuario = self.values['usuario']
            senha = self.values['senha']
            usuario_referencia = self.values['usuario_referencia']

            '''instanciando o objeto da classe InstaBot para usar executar os
            metodos pertinenetes a ela'''
            bot_insta = InstaBot()
            bot_insta.usuario = usuario
            bot_insta.senha = senha
            bot_insta.usuario_referencia = usuario_referencia

            if bot_insta.valida_senha():
                bot_insta.login()
                print('Login efetuado com sucesso')
                sleep(3)
                bot_insta.procurar_referencia()
                print('Acessando o perfil de referência')
                sleep(2)
                seguidos = bot_insta.seguir_usuarios()
                print(f'foram seguidos {seguidos} novos usuários')
            else:
                print('Problemas no usuário ou senha')


interface = Interface()
interface.iniciar()
