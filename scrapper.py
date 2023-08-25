import requests
from bs4 import BeautifulSoup
import sqlite3
from selenium import webdriver


driver = webdriver.Chrome(executable_path='chromedriver')
import time
time.sleep(5)

driver.get('https://www.glassdoor.co.in/Job/index.htm')

print(driver)

email_field = driver.find_element_by_id('modalUserEmail')
email_field.send_keys('www.anuragtiwari23@gmail.com') 
next_button = driver.find_element_by_css_selector('[data-testid="email-form-button"]')
next_button.click()

password_field = driver.find_element_by_id('inlineUserPassword')
password_field.send_keys('Danurag23@')  
login_button = driver.find_element_by_css_selector('[name="submit]')
login_button.click()




conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

#
cursor.execute('''
    CREATE TABLE IF NOT EXISTS glassdoor_api_company (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        rating REAL,
        review_count INTEGER
    )
''')


base_url = 'https://www.glassdoor.com/Reviews/index.htm?page={}'
page_number = 1

while True:
    
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    info = soup.find_all(attrs={'data-test': 'employer-card-single'})
    print(info)


    for company_data in soup.find_all('div', class_='company-data'):
        name = company_data.find('span', class_='company-name').text
        rating = float(company_data.find('span', class_='rating').text)
        review_count = int(company_data.find('span', class_='review-count').text.replace(',', ''))
        print(name)
        print(rating)
        print(review_count)
        cursor.execute('''
            INSERT INTO glassdoor_api_company (name, rating, review_count)
            VALUES (?, ?, ?)
        ''', (name, rating, review_count))

    # 
    conn.commit()

  
    next_button = soup.find('a', class_='next')
    if not next_button:
        break

    
    page_number += 1

#
conn.close()

# Close
driver.quit()
