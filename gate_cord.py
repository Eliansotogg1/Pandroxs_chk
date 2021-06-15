from copy import error
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
import sys

class Gate_cord:

    def __init__(self):
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
        self.__driver = webdriver.Chrome(path, options=self.chrome_options)   #Crea interfaz con las opciones
        self.__driver.get("https://www.cort.com/furniture-rental/living-room-tvs/P1504336")  #Carga la web 
        self.add_product()
        #timer0 = threading.Timer(4, self.add_product())
        #timer0.start()

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
        #self.chrome_options.add_argument("--headless")                  #Ocultar navegador
        self.chrome_options.add_argument('--no-sandbox')               #Only linux
        self.chrome_options.add_argument('--ignore-certificate-errors')
        self.chrome_options.add_argument('--disable-dev-shm-usage')

        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    def add_product(self):
        error = False
        try:
            WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div/app-pdp/app-pdp-check-availability/form/div/div/div[2]/div/input')))
        except:
            error = True
            print(Fore.RED, 'ERROR TO LOAD PAGE', Fore.WHITE)
        
        if error == False:
            self.__driver.find_element_by_xpath('/html/body/app-root/div/div/app-pdp/app-pdp-check-availability/form/div/div/div[2]/div/input').click()
            self.__driver.find_element_by_xpath('/html/body/app-root/div/div/app-pdp/app-pdp-check-availability/form/div/div/div[2]/div/input').send_keys('75050')
            self.__driver.find_element_by_xpath('/html/body/app-root/div/div/app-pdp/app-pdp-check-availability/form/div/div/div[4]/button').click()
            sleep(4)
            self.__driver.find_element(By.CLASS_NAME, 'pdp_button').click()
            #self.__driver.find_element(By.XPATH, ".//div[contains(@class, 'pdp_button')]").click()
            sleep(4)
            self.__driver.find_element_by_xpath('//*[@id="offCanvas"]/div[4]/div/div[2]/div/div[2]/a').click()
            sleep(6)
            self.__driver.find_element_by_xpath("/html/body/app-root/div/div/app-cart/main/div[3]/div[2]/div/div[3]/div[7]/button").click()
            sleep(6)
            self.__driver.find_element_by_xpath('/html/body/app-root/div/div/app-login/main/div[2]/div[1]/form/label/input').send_keys('sadabdhads@gmail.com')
            sleep(6)
            self.__driver.find_element_by_xpath('/html/body/app-root/div/div/app-login/main/div[2]/div[1]/form/div[3]/button')

gate = Gate_cord()












