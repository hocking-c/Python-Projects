from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Keep browser window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get Cookie to click on
cookie = driver.find_element(By.ID, "cookie")
cookie.click()

# Get upgrade item IDs
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    # Every 5 minutes
    if time.time() > timeout:

        # Get all upgrade <b> tags
        prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # Convert <b> text into integer price
        for price in prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create a dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase most expensive and affordable upgrade
        highest_price_upgrade = max(affordable_upgrades)
        print(highest_price_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until next check
        timeout = time.time() + 5

    # After 5 minutes stop bot and check cookie count
    if time.time() > five_min:
        cookie_per_second = driver.find_element(By.ID, "cps").text
        print(cookie_per_second)
        break
