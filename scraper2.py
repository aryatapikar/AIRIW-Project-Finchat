import requests
from bs4 import BeautifulSoup

# Specify the URL of the website you want to scrape
url = "https://www.investopedia.com/articles/basics/06/invest1000.asp"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, "html.parser")

# Find all headers (h2) and paragraphs (p)
headers = soup.find_all("h2")

# Iterate over each header
for header in headers:
    # Print the header text
    print("Header:", header.text.strip())
    
    # Find the next sibling of the header until the next header is encountered
    next_element = header.find_next_sibling()
    
    # Loop until next header is encountered or until there's no next element
    while next_element and next_element.name != "h2":
        # Check if the next element is a paragraph
        if next_element.name == "p":
            # Print the paragraph text
            print("Paragraph:", next_element.text.strip())
        
        # Move to the next sibling
        next_element = next_element.find_next_sibling()
    
    # Add a newline for better readability
    print()
