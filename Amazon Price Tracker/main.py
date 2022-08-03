from bs4 import BeautifulSoup
import requests
import smtplib

USER_PRICE = 128900.00
AMAZON_URL = "https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5T2XSF/ref=" \
             "sr_1_2_sspa?crid=BYD93XZSPIG6&dchild=1&keywords=iphone+12+pro+max&qid=" \
             "1630074477&s=electronics&sprefix=iphone+12%2Celectronics%2C305&sr=" \
             "1-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNDdQTlVITUtSTDdPJmVuY3J5cHRlZElk" \
             "PUEwNjg2MTg3M1ZVVDVXRU9YV1dFMCZlbmNyeXB0ZWRBZElkPUEwMDU5MTcyQU40RjBINkM0SUtTJndpZGdl" \
             "dE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

MY_EMAIL = "email"
PASSWORD = "password"
SUBJECT = "Amazon Price Alert!!"

response = requests.get(AMAZON_URL, headers=headers)
amazon_html = response.text

soup = BeautifulSoup(amazon_html, "html.parser")

price_tag = soup.find(name="span", id="priceblock_dealprice")
price_with_currency = price_tag.getText()

title = soup.find(name="span", id="productTitle").getText().replace("\n", "")

price_with_comma = price_with_currency.split("₹")[1]
price = float(price_with_comma.replace(",", ""))

if price < USER_PRICE:
    print("It is affordable")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:{SUBJECT}\n\n{title} is now available at Rs.{price_with_comma}\n{AMAZON_URL}"
        )

        print("Email Sent!")
