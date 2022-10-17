from selenium import webdriver
import time

veri = input("#Arama : ")
browser = webdriver.Firefox(executable_path=r"C:\Users\Thunder\Desktop\geckodriver.exe")
browser.get("https://twitter.com/search?q="+veri+"&src=typed_query&f=live")
browser.maximize_window()
time.sleep(2)

sonuc = []
twit = browser.find_elements_by_xpath("//div[@data-testid='tweetText']")
time.sleep(2)
print("------------------------------\n" + str(len(twit)) + "adet twit başarıyla çekildi \n------------------------------")
for i in twit:
    sonuc.append(i.text)

sayac = 0
son = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    if sayac > 3 :
        break
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(2)
    yeni = browser.execute_script("return document.documentElement.scrollHeight")
    if son == yeni :
        break
    son = yeni
    sayac += 1
    twit = browser.find_elements_by_xpath("//div[@data-testid='tweetText']")
    time.sleep(2)
    print("------------------------------\n" + str(len(twit)) + "adet twit başarıyla çekildi \n------------------------------")
    for i in twit:
        sonuc.append(i.text)

adet = 1
with open("twitler.txt","w",encoding="UTF-8") as file :
    for a in sonuc :
        file.write(f"{adet} - {a}\n")
        adet += 1
print("twitler.txt dosyasına twitler başarı ile kaydedildi")