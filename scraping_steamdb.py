from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd


driver = webdriver.Chrome()
driver.get("https://steamdb.info/sales/")
time.sleep(5)


names = []
discounts = []
prices = []
ratings = []
release_dates = []

while True:

    WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tr.app")))

    rows = driver.find_elements(By.CSS_SELECTOR, "tr.app")

    for row in rows:
        name = row.find_element(By.CSS_SELECTOR, "a.b").text.strip()
        discount = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[1].text.strip()
        price = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[2].text.strip()
        rating = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[3].text.strip()   
        release_date = row.find_elements(By.CSS_SELECTOR, "td.dt-type-numeric")[4].text.strip()
        
        names.append(name)
        discounts.append(discount)
        prices.append(price)
        ratings.append(rating)
        release_dates.append(release_date)
        
    data = {
        "Game Name": names,
        "Discount": discounts,
        "Price": prices,
        "Rating": ratings,
        "Release Date": release_dates
        }
        
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.dt-paging-button.next"))
        )

        if "disabled" in next_button.get_attribute("class"):
            print("Última página alcançada.")
            break
            
        next_button.click()  
        time.sleep(5)  
        
    except TimeoutException:
        print("Última página alcançada ou botão 'Next' não encontrado.")
        break

driver.quit()

df = pd.DataFrame(data)
df['row_id'] = df.index + 1
reorder = ['row_id', 'Game Name', 'Discount', 'Price', 'Rating', 'Release Date']
df = df[reorder]

df.to_csv('steamdb_sales.csv', index=False)

