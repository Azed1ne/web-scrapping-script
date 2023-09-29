from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# Creating a service object to set up the driver with new webDriver build that hasn't released yet
service = Service(r"INSERT_PATH_TO_chromedriver.exe")
driver = webdriver.Chrome(service=service)


# Navigate to the website
driver.get("https://airtable.com")

# Wait for the page to load
time.sleep(10)


x=0
while x<=30:
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    project_elements = soup.find_all("div", {"class": "rowSuggestion"}) # Project Names: rowSuggestion // Names: rowSuggestion baymax

    # Printing project names, will be using another tool to remove duplicates
    for project_element in project_elements:
        print(project_element.find("div", {"class": "flex-auto truncate"}).get_text())
    time.sleep(0.5) # time so the user scrolls manually

# Closing the web driver
driver.quit()
