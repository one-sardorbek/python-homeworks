import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup

def scrape_laptops():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    chrome_options = Options()
    driver = webdriver.Chrome(chrome_options)
    
    driver.get("https://www.demoblaze.com/")
    time.sleep(3)
    
    # Click on Laptops category
    driver.find_element(By.LINK_TEXT, "Laptops").click()
    time.sleep(3)
    
    laptops = []
    
    while True:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        items = soup.find_all("div", class_="card-block")
        
        for item in items:
            name = item.find("h4", class_="card-title").text.strip()
            price = item.find("h5").text.strip()
            description = item.find("p", class_="card-text").text.strip()
            
            laptops.append({"name": name, "price": price, "description": description})
        
        # Try clicking Next button
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            next_button.click()
            time.sleep(3)
        except:
            break  # No more pages
    
    driver.quit()
    return laptops

def save_to_json(data, filename="laptops.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

def main():
    laptops = scrape_laptops()
    save_to_json(laptops)

if __name__ == "__main__":
    main()
