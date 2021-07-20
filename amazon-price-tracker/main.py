from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
my_email = ""
password = ""
recipient = ""
EXPECTED_PRICE = 70

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    "Accept-Language": "en-us"
}

response = requests.get("https://www.amazon.com/dp/B07ZCTW9FZ/?coliid=I2MH3OFCHBCAH5&colid=3ML687DPW7U41&psc=1&ref_=lv_ov_lig_dp_it", headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")

price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")


item_price = price.getText()
item_price = float(item_price.split("$")[1])
print(item_price)

if item_price < EXPECTED_PRICE:
    print("TRUE")
    with smtplib.SMTP("smtp.gmail.com", "587") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient,
            msg=f"Subject:PRICE DROP!\n\nYour item's price has lowered!"
        )