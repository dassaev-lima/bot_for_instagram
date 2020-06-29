from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
        self.usuario = ''
        self.senha = ''
        self.usuario_referencia = ''
        self.site = 'https://www.instagram.com'
    
    def login(self):
        self.driver.get(self.site)
        sleep(2)
        
        campo_usuario = self.driver.find_element_by_xpath(f"//input[@name='username']")
        sleep(2)
        campo_usuario.send_keys(self.usuario)
        campo_senha = self.driver.find_element_by_xpath("//input[@aria-label='Senha']")
        sleep(2)
        campo_senha.send_keys(self.senha)
        campo_senha.send_keys(Keys.RETURN)

    def valida_senha(self):
        return len(self.senha) > 5
    
    def procurar_referencia(self):
        campo_pesquisar = self.driver.find_element_by_xpath("//input[@placeholder='Pesquisar']")
        sleep(3)
        campo_pesquisar.send_keys(self.usuario_referencia)
        sleep(3)
               
        perfil_pesquisado = self.driver.find_element_by_xpath(f"//a[@href='/{self.usuario_referencia}/']")
        sleep(2)
        perfil_pesquisado.click()


    def seguir_usuarios(self):

        menu_seguidores = self.driver.find_element_by_xpath(f"//a[@href='/{self.usuario_referencia}/followers/']")
        sleep(3)
        menu_seguidores.click()
        sleep(3)

        #for x in range(1,3):
        #    self.driver.execute_script("window.scrollTop(0, document.body.scrollHeigh);")
        #    sleep(2)
        
        lista_botoes_seguir = self.driver.find_elements_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        sleep(3)

        for elem in lista_botoes_seguir:
            elem.click()
            sleep(1)
      
    
        
  
       



