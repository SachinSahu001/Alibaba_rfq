# scraper.py

import csv
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

# Constants
URL_TEMPLATE = "https://sourcing.alibaba.com/rfq/rfq_search_list.htm?country=AE&recently=Y&page={}"
OUTPUT_FILE = "data/output.csv"
MAX_PAGES = 3

def get_driver():
    options = uc.ChromeOptions()
    options.add_argument("--headless=new")  # Comment this if you want to see the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = uc.Chrome(options=options)
    return driver

def extract_rfq_data(rfq):
    try:
        product_name = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__subject").text.strip()
    except:
        product_name = ""

    try:
        description = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__detail").text.strip()
    except:
        description = ""

    try:
        quantity = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__quantity").text.strip()
    except:
        quantity = ""

    try:
        unit = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__unit").text.strip()
    except:
        unit = ""

    try:
        country = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__country").text.strip()
    except:
        country = ""

    try:
        date_posted = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__date").text.strip()
    except:
        date_posted = ""

    try:
        quotes_left = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__quote-num").text.strip()
    except:
        quotes_left = ""

    try:
        buyer_name = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__buyer-name").text.strip()
    except:
        buyer_name = ""

    try:
        email_verified = rfq.find_element(By.CLASS_NAME, "brh-rfq-item__email-verified").text.strip()
    except:
        email_verified = ""

    return [
        product_name, description, quantity, unit,
        country, date_posted, quotes_left, buyer_name, email_verified
    ]

def scrape():
    driver = get_driver()
    all_data = []

    for page in range(1, MAX_PAGES + 1):
        print(f"Scraping page {page}...")
        driver.get(URL_TEMPLATE.format(page))

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[contains(@class, "brh-rfq-item") and contains(@class, "container")]')
                )
            )
            rfqs = driver.find_elements(By.XPATH, '//div[contains(@class, "brh-rfq-item") and contains(@class, "container")]')
            print(f"✅ Found {len(rfqs)} RFQs")
        except Exception as e:
            print(f"❌ Failed to scrape page {page}: {e}")
            continue

        for rfq in rfqs:
            all_data.append(extract_rfq_data(rfq))

        time.sleep(2)  # Be polite to the server

    driver.quit()

    if all_data:
        with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Product Name", "Description", "Quantity", "Unit", "Country", "Date Posted", "Quotes Left", "Buyer Name", "Email Verified"])
            writer.writerows(all_data)
        print(f"✅ Saved {len(all_data)} rows to {OUTPUT_FILE}")
    else:
        print("⚠️ No data to write.")

if __name__ == "__main__":
    scrape()
