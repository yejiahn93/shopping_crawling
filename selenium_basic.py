from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/yejiahn/Downloads/chromedriver')

browser.get('https://shopping.google.com/?nord=1')


#browser.find_element_by_css_selector('a.nav.shop').click

#search click

search = browser.find_element_by_css_selector('input.r7gAOb.yyJm8b')
search.click()

#search item
search.send_keys('iphone 13 promax')
search.send_keys(Keys.ENTER)