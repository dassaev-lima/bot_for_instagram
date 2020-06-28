from insta_bot import InstaBot
from time import sleep

if __name__ == "__main__":
    instagram_bot = InstaBot()

    if instagram_bot.valida_senha():
        instagram_bot.login()
        sleep(3)
        instagram_bot.procurar_referencia()
        sleep(2)
        instagram_bot.seguir_usuarios()
    else:
        print('Problemas no usuário ou senha')
