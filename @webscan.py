import requests
from bs4 import BeautifulSoup

def fetch_all_links(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all <a> tags with href attributes
        a_tags = soup.find_all('a', href=True)
        
        # Find all <link> tags with href attributes
        link_tags = soup.find_all('link', href=True)
        
        # Extract and print the URLs from <a> tags
        print(f"Links found on {url}:")
        for tag in a_tags:
            print(f"a tag: {tag['href']}")
        
        # Extract and print the URLs from <link> tags
        for tag in link_tags:
            print(f"link tag: {tag['href']}")
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the URL you want to fetch links from
    url = input("Enter the URL of the webpage: ")
    fetch_all_links(url)

