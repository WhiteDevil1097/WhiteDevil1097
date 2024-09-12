import requests
from bs4 import BeautifulSoup

def get_web_data(url):
    try:
        # Send a GET request to the website
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the webpage content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Print the title of the webpage
            title = soup.title.string
            print(f"Page Title: {title}")
            
            # Get all text content from the webpage
            page_text = soup.get_text()
            print("\nPage Content:\n")
            print(page_text)
        else:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt the user to enter a URL
    url = input("Enter the URL of the webpage to scrape: ")
    get_web_data(url)

