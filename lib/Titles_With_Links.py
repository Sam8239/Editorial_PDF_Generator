from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

title_to_link = {}


def Titles_With_Links():
    # Specify the path to the Chrome web driver executable
    driver_path = "C:/webdrivers/chromedriver"

    # Create a Service object for the Chrome web driver
    service = Service(driver_path)

    # Create an instance of the Chrome web driver
    driver = webdriver.Chrome(service=service)

    # Navigate to the Hindustan Times editorials page
    driver.get("https://www.hindustantimes.com/editorials")

    # Extract the HTML content of the page
    content = driver.page_source

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    for h in soup.findAll("h3", attrs={"class": "hdg3"}):
        title = h.text.strip()
        link = h.find("a")["href"]
        title_to_link[title] = link

    # Close the web driver
    driver.quit()
    return title_to_link
