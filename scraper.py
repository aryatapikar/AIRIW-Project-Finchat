from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from file_name_gen import generate_file_name

# Set up Selenium webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
driver = webdriver.Chrome(options=chrome_options)

# Specify the website you want to scrape
url = "https://www.investopedia.com/terms/f/financial-analysis.asp"
# Load the page
driver.get(url)

# Get the page source
page_source = driver.page_source

# Close the webdriver
driver.quit()

# Parse the HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Find the desired elements
div_texts = soup.find_all('p')

# If the elements are found, write their text content to a text file
if div_texts:
    file_name = generate_file_name(url)
    with open(file_name, "w") as file:
        for div_text in div_texts:
            file.write(div_text.get_text() + "\n")
    print("Content written to", file_name, "successfully.")
else:
    print("Element not found.")
