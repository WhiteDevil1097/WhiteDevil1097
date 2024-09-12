import requests
import os
from bs4 import BeautifulSoup

def get_links(url):
    # Send a GET request
    response = requests.get(url)
    
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        page_content = response.content
        
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Find all links on the page
        links = soup.find_all('a')
        
        # Return the list of links
        return [link.get('href') for link in links]
    else:
        return []

# Main function
def main():
    # URL of the webpage to scrape
    url = "http://www.google.com"
    
    # Get the links
    links = get_links(url)
    
    # Print the links
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
