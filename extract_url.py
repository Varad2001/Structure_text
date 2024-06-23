import requests
from bs4 import BeautifulSoup

def extract_content_from_webpage(url):
    # Fetch the webpage content
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch webpage: {url}")
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract elements
    content = {
        "headings": [],
        "subheadings": [],
        "paragraphs": [],
        "page_numbers": []
    }
    
    for tag in soup.find_all(['h1']):
        content["headings"].append(tag.get_text(strip=True))
    
    for tag in soup.find_all(['h4', 'h5', 'h6', 'h2', 'h3']):
        content["subheadings"].append(tag.get_text(strip=True))
    
    for tag in soup.find_all('p'):
        content["paragraphs"].append(tag.get_text(strip=True))
    
    
    for tag in soup.find_all('span', class_='page-number'):
        content["page_numbers"].append(tag.get_text(strip=True))
    
    return content


if __name__ == "__main__":
    
    
    url = 'https://en.wikipedia.org/wiki/Light-year'
    content = extract_content_from_webpage(url)
    print("Headings:", content["headings"])
    print("Subheadings:", content["subheadings"])
    print("Paragraphs:", content["paragraphs"])
    print("Page Numbers:", content["page_numbers"])
