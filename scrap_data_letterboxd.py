from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from collections import Counter
import time


def get_word_counts(movie):
    movie = "-".join(movie.split())
    word_list = []
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension('Extensions/uBlock-Origin.crx')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    url ="https://letterboxd.com/film/"+movie+"/reviews/by/activity/page/"
    for page_number in range(1, 5):
        current_url = f"{url}{page_number}/"
        driver.get(current_url)
        posts = driver.find_elements(By.CLASS_NAME, "body-text.-prose.collapsible-text")
        for content in posts:
            text = content.text
            words = text.split()
            for word in words:
                word = word.lower()
                word_list.append(word)
    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts

def get_word_counts_user(username):

    word_list = []
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_extension('Extensions/uBlock-Origin.crx')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    url ="https://letterboxd.com/"+username+"/films/reviews/page/"
    for page_number in range(1, 10):
        current_url = f"{url}{page_number}/"
        driver.get(current_url)
        posts = driver.find_elements(By.CLASS_NAME, "body-text.-prose.collapsible-text")
        for content in posts:
            text = content.text
            words = text.split()
            for word in words:
                word = word.lower()
                word_list.append(word)
    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts






