from selenium import webdriver

chrome_driver_path = "/Users/pow/Desktop/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)
# driver.close()
events = {}
event_times = driver.find_elements_by_css_selector(".event-widget time")


event_names = driver.find_elements_by_css_selector(".event-widget li a")
# for details in event_texts:
#     print(details.text)

for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text
    }

print(events)
# date5 = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/time')
# print(date1.text)
#
# event5 = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li[1]/a')
# print(event1.text)


driver.quit()