from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from file_name_gen import generate_file_name

# Set up Selenium webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headless Chrome
driver = webdriver.Chrome(options=chrome_options)

# Specify the website you want to scrape
url = "https://www.capitalone.com/learn-grow/money-management/money-management-tips/"
# Load the page
driver.get(url)

# Get the page source
page_source = driver.page_source

# Close the webdriver
driver.quit()

# Parse the HTML
soup = BeautifulSoup(page_source, 'html.parser')

# Find all headings (h1, h2, h3, etc.) and paragraphs (p)
headings = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
paragraphs = soup.find_all("p")

# If both headings and paragraphs are found, write their text content to a text file
if headings and paragraphs:
    file_name = generate_file_name(url)
    with open(file_name, "w") as file:
        # Write headings first
        for heading in headings:
            file.write(heading.get_text().strip() + "\n\n")
        # Write paragraphs
        for paragraph in paragraphs:
            file.write(paragraph.get_text().strip() + "\n\n")
    print("Content written to", file_name, "successfully.")
else:
    print("Headings or paragraphs not found.")
