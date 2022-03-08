# shopping_crawling
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv

browser = webdriver.Chrome('/Users/yejiahn/Downloads/chromedriver')

browser.get('https://shopping.google.com/?nord=1')


#browser.find_element_by_css_selector('a.nav.shop').click

#search click

search = browser.find_element_by_css_selector('input.r7gAOb.yyJm8b')
search.click()

#search item
search.send_keys('iphone 13 promax')
search.send_keys(Keys.ENTER)

#infinity scroll
before_h = browser.execute_script("return window.scrollY")
while True:
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    time.sleep(2)

    after_h = browser.execute_script("return window.scrollY")
    if after_h == before_h:
        break

    before_h = after_h


f = open(r"/Users/yejiahn/Desktop/projects/shopping_crawling/data.csv", 'w', encoding='CP949')
csvWriter = csv.writer(f)

items = browser.find_elements_by_css_selector(".KZmu8e")

for item in items:
    name = item.find_element_by_css_selector(".sh-np__product-title.translate-content").text
    try:
        price = item.find_element_by_css_selector(".hn9kf").text
    except:
        price = "NA"
    label = item.find_element_by_css_selector(".sh-np__seller-container").text
    print(name, price, label)
    csvWriter.writerow([name,price,label])

f.close()
