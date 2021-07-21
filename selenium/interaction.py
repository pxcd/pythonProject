import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/pow/Desktop/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")




# article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# article_count = driver.find_elements_by_css_selector("#articlecount a")
# article_count.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search_box = driver.find_element_by_name("search")
# search_box.send_keys("python")
# search_box.send_keys(Keys.ENTER)


# driver.quit()
# driver.get("http://secure-retreat-92358.herokuapp.com")
# fname = driver.find_element_by_name("fName")
# fname.send_keys("paolo")
# lname = driver.find_element_by_name("lName")
# lname.send_keys("dizon")
# email = driver.find_element_by_name("email")
# email.send_keys("pow@email.com")
#
# submit = driver.find_element_by_xpath('/html/body/form/button')
# submit.click()


driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_css_selector("#bigCookie")

# rate = driver.find_elements_by_css_selector("")
# cookies = driver.find_element_by_css_selector("#cookies")
# cookie_text = cookies.text
# cookie_number = int(cookie_text.split(" ")[0])

timeout = time.time() + 5
while True:
    cookie.click()
    # if time.time() > timeout:
    #     powerup3 = driver.find_elements_by_css_selector("#product3")
    #     powerup3.click()
    #
    #     powerup2 = driver.find_elements_by_css_selector("#product2")
    #     powerup2.click()
    #
    #     powerup1 = driver.find_elements_by_css_selector("#product1")
    #     powerup1.click()
    #
    #     powerup0 = driver.find_elements_by_css_selector("#product0")
    #     powerup0.click()






