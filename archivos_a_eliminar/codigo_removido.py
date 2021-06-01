
#Codigo para resolver el captcha
'''
#captcha
    captchalink = ""
    encode2 = ''
    cadena = ""
    d = ""
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
        solvecaptcha2()'''

'''
#Velocidad de carga para la fucion textito
loading_speed = 30
loading_string = "." * 3
# Funcion no utilizada
def textito(texto):
    
        #Toma el texto y lo imprime caracter por caracter
        #en consola, limpiando el bufer
    

    global loading_speed
    loading = True
    while loading:
        for index, char in enumerate(texto):
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(1.0 / loading_speed)
            loading = False
'''