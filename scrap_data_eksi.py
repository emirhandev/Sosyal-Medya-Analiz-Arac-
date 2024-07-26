from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from collections import Counter

def get_word_counts(url):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    word_list = []
    driver.get(url)
    driver_url = driver.current_url
    url = driver_url
    for page_number in range(1, 10):
        print(page_number, ". numaralı sayfa taranıyor...")
        current_url = f"{url}?p={page_number}"
        driver.get(current_url)
        posts = driver.find_elements(By.CLASS_NAME, "content")

        for content in posts:
            text = content.text
            words = text.split()
            for word in words:
                if not word.startswith("http") and "bkz" not in word:
                    word = word.lower()
                    word_list.append(word)

    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts

def get_word_counts_user(url):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    word_list = []

    driver.get(url)
    posts = driver.find_elements(By.CLASS_NAME, "content")
    for content in posts:
        text = content.text
        words = text.split()
        for word in words:
            if not word.startswith("http") and "bkz" not in word:
                word = word.lower()
                word_list.append(word)

    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts