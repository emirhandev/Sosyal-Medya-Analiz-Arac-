import matplotlib.pyplot as plt
import sendMailSystem as sms
from collections import Counter
import time
from tkinter import *
from tkinter import messagebox
def visualize(sorted_word_counts,platform):
    words, counts = zip(*sorted_word_counts[:20])
    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.xlabel('Kelimeler')
    plt.ylabel('Kullanım Miktarı')
    plt.title(platform+' En Fazla Kullanılan Kelimelerin Grafiği')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('report.png')
    plt.show()
    time.sleep(5)
    sms.send_email()
    messagebox.showinfo("Sosyal Medya Analiz Aracı", "Sosyal Medya Analiz Raporunuz E-Postanıza Gönderildi")






