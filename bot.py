from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# inicjalizacja sterownika przeglądarki Chrome
chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=chrome_options)

# Otwarcie strony RedBull
driver.get('https://www.redbull.com/pl-pl/projects/super-dzien')

# Zamknij cookies
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()

# Klinik przycisk  rozwiąż quiz
WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="button button--clickable button--cta"]'))).click()

# znajdź ikonę z Mają Kuczyńską i go kliknij
button = driver.find_element(By.ID, 'hero3')
driver.execute_script("arguments[0].click();", button)

if driver.current_url == 'https://www.redbull.com/pl-pl/projects/super-dzien#contest-details-content': # <---- jeśli znajdziesz się na stronie to:
    
    responses = ("Tak", "Nie ma takiego rozróżnienia", "SGH", "2010", "4x15 min / dzień", "8-way", "113", 
    "Skleja modele samolotów", "Z pilotem akrobacyjnym Łukaszem Czepielą", "Nigdy nie brała udziału w takich zawodach", 
    "Zajęłaby się ekonomią", "2015", "6", "10 m", "Tak, skacze od dawna", "Skoku na spadochronie w tandemie", "Występować w filmowych superprodukcjach",
    "1964 r", "1964 r", "Dubaju", "FlySpot", "Dynamic", "Kyra Poh", "Lot swobodny w tunelu aerodynamicznym")
    question_num = 100
    for x in range(question_num): # <---- powiel 100 razy
        for response in responses: # <---- dla każdej odpowiedzi z 'responses'
            try:
                button = driver.find_element(By.XPATH, f'//div[text() = "{response}"]') # <------- znajdź element zawierający odpowiedź
                driver.execute_script("arguments[0].click();", button) # <---- i go kliknij
            except:
                pass # <----- jeśli nie znajdziesz elementu to go pomiń