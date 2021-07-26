from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

# listing_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
listing_url = "https://www.zillow.com/homes/for_rent/3-_beds/2.0-_baths/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.61529005957031%2C%22east%22%3A-122.25136794042969%2C%22south%22%3A37.62561604480192%2C%22north%22%3A37.92466445294142%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%2C%22min%22%3A823461%7D%2C%22beds%22%3A%7B%22min%22%3A3%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%2C%22min%22%3A2000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22baths%22%3A%7B%22min%22%3A2%7D%7D%2C%22isListVisible%22%3Atrue%7D"
forms_url = "https://docs.google.com/forms/d/1RD_Rp03yxhuNQMLTCcrp6cj5a0JOmEYuBvDRkHTzm1c/edit"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Accept-Language": "en-us"
}

chrome_driver_path = "/Users/pow/Desktop/chromedriver"

response = requests.get(url=listing_url, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")

prices = []
rent_prices = soup.find_all(name="div", class_="list-card-price")

for price in rent_prices:
    prices.append(price.getText())



addresses = []
rent_addresses = soup.find_all(name="address", class_="list-card-addr")
for address in rent_addresses:
    addresses.append(address.getText())


urls = []
rent_urls = soup.find_all(name="a", class_="list-card-link list-card-link-top-margin")
for url in rent_urls:
    urls.append(url.get("href"))

# print(prices)
# print(addresses[0])
# print(urls)
# print(len(prices))
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(forms_url)

for n in range(len(prices)):
    print(f"run number {n}")
    time.sleep(1)
    address_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.click()
    address_field.send_keys(addresses[n])
    price_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.click()
    price_field.send_keys(prices[n])
    url_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    url_field.click()
    url_field.send_keys(urls[n])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    another = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another.click()
    time.sleep(2)
    if n == len(prices)-1:
        driver.get("https://docs.google.com/forms/d/1RD_Rp03yxhuNQMLTCcrp6cj5a0JOmEYuBvDRkHTzm1c/edit")
        edit_form = driver.find_element_by_xpath('/html/body/div/div[1]/div/span/span[2]/div')
        edit_form.click()
        responses = driver.find_element_by_xpath('//*[@id="tJHJj"]/div[3]/div[1]/div/div[2]/span/div')
        responses.click()
        create_spreadsheet = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div/div[1]')
        create_spreadsheet.click()






