import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import sys
import time
def animated(text):
     for x in text:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)

logo = '''
______                  ______ _____  
|   __ \.--.--.-----.  |      |  |  | 
|   __ <|  |  |  _  |__|  --  |__    |
|______/|_____|___  |__|______|  |__| 
              |_____|                 
'''
animated(logo)
print('      »»»Coder By White_Devil««« ')
def is_valid(url):
    """
    Checks whether the URL is valid and has a valid scheme (http, https).
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_links(url):
    """
    Returns all the URLs found on a web page.
    """
    urls = set()
    domain_name = urlparse(url).netloc
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if is_valid(href) and domain_name in href:
            urls.add(href)
    return urls

def check_link(url):
    """
    Checks the status code of a URL to determine if it's working.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

def find_broken_links(url):
    """
    Crawls the provided URL and identifies broken links.
    """
    broken_links = []
    urls = get_all_links(url)
    print(f"Found {len(urls)} links on {url}.")
    
    for link in urls:
        if not check_link(link):
            broken_links.append(link)
    
    return broken_links

if __name__ == "__main__":
    target_url = "https://www.google.com/"  # Replace with the target website
    broken_links = find_broken_links(target_url)
    
    if broken_links:
        print("Broken links found:")
        for link in broken_links:
            print(link)
    else:
        print("No broken links found.")

