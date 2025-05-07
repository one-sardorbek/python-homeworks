from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json

# Configure Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

urls={

"Mandarin" : "https://www.google.ca/maps/place/Mandarin+Restaurant/@43.7058795,-79.4030938,17z/data=!3m1!5s0x882b333c92642ff7:0x62428c6b425ca338!4m8!3m7!1s0x882b333c94368f83:0x9aef5d84ae16fd5e!8m2!3d43.7058794!4d-79.3983291!9m1!1b1!16s%2Fg%2F1hm3k_jzd?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoJLDEwMjExNDUzSAFQAw%3D%3D",
"Chi_Dim_Sum" : "https://www.google.ca/maps/place/Chi+Dim+Sum/@43.7106336,-79.4752157,13z/data=!4m7!3m6!1s0x882b336953c7b3cd:0xce759d3b426c75ef!8m2!3d43.7106435!4d-79.3988374!15sCgtSZXN0YXVyYW50c1oVIhNjaGluZXNlIHJlc3RhdXJhbnRzkgESY2hpbmVzZV9yZXN0YXVyYW50qgFeCggvbS8wMXh3ORABKhciE2NoaW5lc2UgcmVzdGF1cmFudHMoADIeEAEiGuInnWVrUEwRITwVosFBOxis3ebJVx8poGpoMhcQAiITY2hpbmVzZSByZXN0YXVyYW50c-ABAA!16s%2Fg%2F11gslt1w3g?entry=tts&g_ep=EgoyMDI1MDQyMy4wIPu8ASoASAFQAw%3D%3D&skid=3cf8be44-54a3-45d1-abdb-36dd764d43b1", 
"Haru_Shabu_Shabu" : "https://www.google.ca/maps/place/Haru+Shabu+Shabu+%E5%B0%8F%E6%98%A5%E6%97%A5%E5%92%8C+%E5%AF%BF%E5%96%9C%E7%83%A7/@43.772743,-79.4230387,16z/data=!3m1!5s0x882b2d6e505cebad:0x7b0ee6f413830cf!4m6!3m5!1s0x882b2d3df75425b9:0x4fedc67eed7ed67a!8m2!3d43.7687022!4d-79.4123463!16s%2Fg%2F11tp6zrsry?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Gols_Lanzhou_Noodle" : "https://www.google.ca/maps/place/Gol's+Lanzhou+Noodle/@43.7780787,-79.4243865,16z/data=!3m1!5s0x882b2d0d9c9a02b7:0xbf78a563b79dba49!4m6!3m5!1s0x882b2d6b281d656b:0xab0b695aadf19590!8m2!3d43.7780847!4d-79.4148122!16s%2Fg%2F11pxnbfylh?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Sang-Ji_Fried_Bao": "https://www.google.ca/maps/place/Sang-Ji+Fried+Bao+(North+York)/@43.7785125,-79.421318,16z/data=!4m6!3m5!1s0x882b2da8c5426cff:0x3eb8bcc5226c20e8!8m2!3d43.7776181!4d-79.414684!16s%2Fg%2F11ghnwpbny?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Noodle_Legand": "https://www.google.ca/maps/place/Noodle+Legend/@43.772743,-79.4230387,16z/data=!3m1!5s0x882b2d6d830dee79:0xd1b34eb5d7626b6!4m6!3m5!1s0x882b2de6cb240a71:0xa0946880edf1dc49!8m2!3d43.7727531!4d-79.4134309!16s%2Fg%2F11t6x0_drh?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"The_Keg_Steakhouse": "https://www.google.ca/maps/place/The+Keg+Steakhouse+%2B+Bar+-+North+York/@43.7612819,-79.4158061,16z/data=!4m6!3m5!1s0x882b2d6f9a44d98d:0x3b0e3ffa409197f2!8m2!3d43.7664579!4d-79.4117723!16s%2Fg%2F11f_f6gg5n?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Cafe_Landwer": "https://www.google.ca/maps/place/Cafe+Landwer/@43.7663338,-79.4219403,16z/data=!4m6!3m5!1s0x882b2d47368b6f81:0x33a49e3734ab2c46!8m2!3d43.7663341!4d-79.4124134!16s%2Fg%2F11j8hkw29v?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Chicken_Plus_The_Bar" : "https://www.google.ca/maps/place/Chicken+Plus+The+Bar/@43.7670001,-79.4181852,16z/data=!4m6!3m5!1s0x882b2d0177435861:0xe18f5525d58db786!8m2!3d43.7642984!4d-79.4108936!16s%2Fg%2F11y29z3j0m?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Grill_Gate" : "https://www.google.ca/maps/place/Grill+Gate/@43.7670001,-79.4181852,16z/data=!4m6!3m5!1s0x882b2d3734626b11:0x1b48278c5f8831fe!8m2!3d43.764221!4d-79.4113256!16s%2Fg%2F11vrhqktj9?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"Hazels_Diner" : "https://www.google.ca/maps/place/Hazel's+Diner/@43.7325992,-79.4087016,17z/data=!4m6!3m5!1s0x882b328d87875495:0x98a4f92594c7a37c!8m2!3d43.7325993!4d-79.403938!16s%2Fg%2F1hc7s9zvf?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D",
"La_Vecchia_Restaurant_Uptown": "https://www.google.ca/maps/place/La+Vecchia+Restaurant+Uptown/@43.7101916,-79.408434,16z/data=!3m1!5s0x882b33230a7c5989:0x40c1dd570c0dd597!4m6!3m5!1s0x882b3323a13c9a6b:0x4ffc81ef9ddbb6e4!8m2!3d43.7101917!4d-79.3988611!16s%2Fg%2F1wbg00sv?entry=ttu&g_ep=EgoyMDI1MDQzMC4xIKXMDSoASAFQAw%3D%3D"


}
google_ids={
    
    "Mandarin":"ChIJg482lDwzK4gRXv0WroRd75o",
    "Chi_Dim_Sum": "ChIJzbPHU2kzK4gR73VsQjuddc4", 
    "Haru_Shabu_Shabu": 'ChIJuSVU9z0tK4gRetZ-7X7G7U8',
    "Gols_Lanzhou_Noodle": "ChIJa2UdKGstK4gRkJXxrVppC6s",
    "Sang-Ji_Fried_Bao": "ChIJ_2xCxagtK4gR6CBsIsW8uD4",
    "Noodle_Legand": "ChIJcQoky-YtK4gRSdzx7YBolKA",
    "The_Keg_Steakhouse": "ChIJ8V5uCXXL1IkRNk8ClsLjfwk",
    "Cafe_Landwer": "ChIJgW-LNkctK4gRRiyrNDeepDM",
    "Chicken_Plus_The_Bar" : "ChIJYVhDdwEtK4gRhreN1SVVj-E",
    "Grill_Gate" : "ChIJEWtiNDctK4gR_jGIX4wnSBs",
    "Hazels_Diner" : "ChIJlVSHh40yK4gRfKPHlCX5pJg",
    "La_Vecchia_Restaurant_Uptown": "ChIJa5o8oSMzK4gR5Lbbne-B_E8"


}



reviews_all = {}

def expand_review_text():
    """Click all 'Read more' buttons on currently loaded reviews"""
    read_more_buttons = driver.find_elements(By.CLASS_NAME, "w8nwRe")
    for button in read_more_buttons:
        try:
            button.click()
            time.sleep(0.2)
        except:
            try:
                driver.execute_script("arguments[0].click();", button)
                time.sleep(0.2)
            except:
                pass

def get_current_reviews():
    """Extract all currently visible reviews"""
    expand_review_text()  # First expand all review text
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    
    reviews = []
    review_elements = driver.find_elements(By.CSS_SELECTOR, 'div.jftiEf')
    
    for element in review_elements:
        try:
            # Use both Selenium and BeautifulSoup for reliability
            element_html = element.get_attribute('outerHTML')
            card = BeautifulSoup(element_html, 'html.parser')
            
            review_id = element.get_attribute('data-review-id') or \
                      card.find('div', class_='MyEned').get('id', None)
            
            author_element = card.find('button', class_='WEBjve')
            author_href = author_element.get('data-href', '') if author_element else ''
            author_id = author_href.split('/')[5] if author_href and len(author_href.split('/')) > 5 else None
            
            name = card.find('div', class_='d4r55').get_text(strip=True) if card.find('div', class_='d4r55') else None
            text = card.find('span', class_='wiI7pd').get_text(strip=True) if card.find('span', class_='wiI7pd') else None
            
            rating_element = card.find('span', {'role': 'img'})
            rating = rating_element.get('aria-label', None) if rating_element else None
            
            reviews.append({
                "google_id": google_ids[restaurant],
                "review_id": review_id,
                "author_id": author_id,
                "name": name,
                "text": text,
                "rating": rating
            })
        except Exception as e:
            print(f"Error processing review: {e}")
            continue
            
    return reviews

def scroll_and_collect_reviews():
    """Scroll through reviews and collect until no new ones appear"""
    collected_reviews = {}
    last_height = 0
    same_height_count = 0
    max_attempts = 30
    
    # First ensure we're on reviews section
    try:
        reviews_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.m6QErb.DxyBCb.kA9KIf.dS8AEf'))
        )
    except:
        print("Could not find reviews section")
        return []
    
    for attempt in range(max_attempts):
        # Get current scroll height
        scroll_height = driver.execute_script("return arguments[0].scrollHeight", reviews_section)
        
        # Scroll down a bit further than last time
        scroll_position = min(last_height + 800, scroll_height)
        driver.execute_script(f"arguments[0].scrollTop = {scroll_position}", reviews_section)
        time.sleep(4)  # Wait for new content to load
        
        # Check if we've reached the bottom
        new_scroll_height = driver.execute_script("return arguments[0].scrollHeight", reviews_section)
        if new_scroll_height == scroll_height:
            same_height_count += 1
            if same_height_count > 3:  # No new content after several attempts
                break
        else:
            same_height_count = 0
        
        # Collect newly loaded reviews
        current_reviews = get_current_reviews()
        for review in current_reviews:
            if review['review_id'] not in collected_reviews:
                collected_reviews[review['review_id']] = review
        
        last_height = scroll_position
        
        # Early exit if we're not making progress
        if attempt > 10 and len(collected_reviews) < 5:
            break
    
    return list(collected_reviews.values())

for restaurant in urls:
    print(f"Scraping reviews for {restaurant}...")
    driver.get(urls[restaurant])
    time.sleep(5)  # Initial load
    
    # Ensure we're on the reviews tab
    try:
        reviews_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(., "Reviews")]'))
        )
        reviews_tab.click()
        time.sleep(3)
    except:
        print(f"Could not click Reviews tab for {restaurant}")
    
    # Collect reviews
    try:
        restaurant_reviews = scroll_and_collect_reviews()
        reviews_all[restaurant] = restaurant_reviews
        print(f"✅ Collected {len(restaurant_reviews)} reviews for {restaurant}")
    except Exception as e:
        print(f"❌ Failed to collect reviews for {restaurant}: {e}")
        reviews_all[restaurant] = []

# Save results
with open("project_py/reviews.json", "w", encoding="utf-8") as f:
    json.dump(reviews_all, f, ensure_ascii=False, indent=4)
    print(f"✅ Saved {sum(len(v) for v in reviews_all.values())} total reviews")

driver.quit()