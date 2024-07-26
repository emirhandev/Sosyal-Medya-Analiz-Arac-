from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import visualize as vs
from collections import Counter
import time

def get_word_counts_facebook(user):
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    word_list = []
    driver.get('https://www.facebook.com/'+user)
    time.sleep(2)
    kapatma_butonu = driver.find_element(By.CSS_SELECTOR,".x1i10hfl.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x87ps6o.x1lku1pv.x1a2a7pz.x6s0dn4.xzolkzo.x12go9s9.x1rnf11y.xprq8jg.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xl56j7k.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.xc9qbxq.x14qfxbe.x1qhmfi1").click()

    for _ in range(10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
    time.sleep(5)
    posts = driver.find_elements(By.CLASS_NAME, 'xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.x126k92a')

    for tweet in posts:
        text = tweet.text
        words = text.split()
        for word in words:
            if not (word.endswith(".")) or  word.endswith(" ,"):
                word = word.lower()
                word_list.append(word)



    driver.quit()
    word_counts = Counter(word_list)
    sorted_word_counts = word_counts.most_common()
    return sorted_word_counts





