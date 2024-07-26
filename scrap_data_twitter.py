from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from collections import Counter
import time

def get_word_counts(word):
    word_list = []
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension('Extensions/uBlock-Origin.crx')
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get("https://twstalker.com/search/" + word)
    wait = WebDriverWait(driver, 20)
    time.sleep(5)
    counter = 0



    tweets = driver.find_elements(By.CLASS_NAME, 'activity-descp')
    for tweet in tweets:
        text = tweet.text
        words = text.split()
        for word in words:
            if not (word.startswith("a") or
                    word.startswith("year") or
                    word.startswith("ago") or
                    word.startswith("hours") or
                    word.startswith("weeks") or
                    word.startswith("Download") or
                    word.startswith("http") or
                    word.startswith("@") or
                    word.startswith("keyboard") or
                    word.startswith("#") or
                    word.startswith("-") or
                    word.startswith("*") or
                    word.startswith("$") or
                    word.startswith("£") or
                    word.startswith("%") or
                    word.isdigit()):
                word = word.lower()
                word_list.append(word)

    time.sleep(10)
    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts

def get_word_counts_user(user):
    word_list = []
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension('Extensions/uBlock-Origin.crx')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    time.sleep(5)
    driver.get("https://twstalker.com/" + user)

    wait = WebDriverWait(driver, 20)
    time.sleep(5)
    counter = 0



    tweets = driver.find_elements(By.CLASS_NAME, 'activity-descp')
    for tweet in tweets:
        text = tweet.text
        words = text.split()
        for word in words:
            if not (word.startswith("a") or
                    word.startswith("year") or
                    word.startswith("ago") or
                    word.startswith("hours") or
                    word.startswith("weeks") or
                    word.startswith("Download") or
                    word.startswith("http") or
                    word.startswith("@") or
                    word.startswith("keyboard") or
                    word.startswith("#") or
                    word.startswith("-") or
                    word.startswith("*") or
                    word.startswith("$") or
                    word.startswith("£") or
                    word.startswith("%") or
                    word.isdigit()):
                word = word.lower()
                word_list.append(word)

    time.sleep(10)
    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts







