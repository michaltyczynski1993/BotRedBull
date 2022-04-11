from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import locators
from selenium.webdriver.common.by import By

class Crawler(object):
    
    
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions(); 
        self.chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
        self.driver = webdriver.Chrome(service=Service('C:\TestFiles\chromedriver.exe'), options=self.chrome_options)

class RedBullCrawler(Crawler):
    """idź do strony Red Bull quiz i zamknij cookies popup"""
    def go_to_website(self):
        self.driver.get('https://www.redbull.com/pl-pl/projects/super-dzien')
        try:
            cookies_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.USER_AGREE)).click()
            cookies_button.click()
        except:
            pass
    
    def go_to_quiz(self):
        """Znajdź przycisk 'rozwiąż quiz' i ikonę Maji Kuczyńskiej"""
        # click on go to quiz button
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locators.QUIZ_BUTTON)).click()
        # find maja Kuczyńska button
        button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(locators.MAJA_BUTTON))
        self.driver.execute_script("arguments[0].click();", button)
    
    def find_answear(self):
        """Jeśli znajdziesz się na stronie quizu znajdź odpowiedzi"""

        if self.driver.current_url == 'https://www.redbull.com/pl-pl/projects/super-dzien#contest-details-content':

            responses = ("Tak", "Nie ma takiego rozróżnienia", "SGH", "2010", "4x15 min / dzień", "8-way", "113", 
            "Skleja modele samolotów", "Z pilotem akrobacyjnym Łukaszem Czepielą", "Nigdy nie brała udziału w takich zawodach", 
            "Zajęłaby się ekonomią", "2015", "6", "10 m", "Tak, skacze od dawna", "Skoku na spadochronie w tandemie", "Występować w filmowych superprodukcjach",
            "1964 r", "1964 r", "Dubaju", "FlySpot", "Dynamic", "Kyra Poh", "Lot swobodny w tunelu aerodynamicznym")

            question_num = 100
            for x in range(question_num):
                for response in responses:
                    try:
                        button = self.driver.find_element(By.XPATH, f'//div[text() = "{response}"]')
                        self.driver.execute_script("arguments[0].click();", button)
                        
                    except:
                        pass

crawler = RedBullCrawler()
crawler.go_to_website()
crawler.go_to_quiz()
crawler.find_answear()