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
        time.sleep(0.02)

logo = '''

   ▄█   ▄█▄    ▄████████  ▄█        ▄█  
  ███ ▄███▀   ███    ███ ███       ███  
  ███▐██▀     ███    ███ ███       ███▌ 
 ▄█████▀      ███    ███ ███       ███▌ 
▀▀█████▄    ▀███████████ ███       ███▌ 
  ███▐██▄     ███    ███ ███       ███  
  ███ ▀███▄   ███    ███ ███▌    ▄ ███  
  ███   ▀█▀   ███    █▀  █████▄▄██ █▀   
  ▀                      ▀              
'''
animated(logo)
print('   [+]»»»Coder By White_Devil«««[+]')

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.RequestException as e:
        print(f"Error: Unable to fetch the webpage content. {e}")
        return None

def extract_title(soup):
    title_tag = soup.title
    return title_tag.string if title_tag else 'No Title Found'

def extract_meta_tags(soup):
    meta_tags = {}
    for meta in soup.find_all('meta'):
        name = meta.get('name')
        content = meta.get('content')
        if name and content:
            meta_tags[name] = content
    return meta_tags

def extract_links(soup, base_url):
    links = set()
    for anchor in soup.find_all('a', href=True):
        href = anchor.get('href')
        full_url = urljoin(base_url, href)
        links.add(full_url)
    return links

def extract_images(soup, base_url):
    images = []
    for img in soup.find_all('img', src=True):
        src = img.get('src')
        alt = img.get('alt', 'No Alt Text')
        full_url = urljoin(base_url, src)
        images.append({'url': full_url, 'alt': alt})
    return images

def main():
    url = input("Enter the URL of the website to scan: ").strip()
    if not url:
        print("URL is required.")
        return

    content = fetch_website_content(url)
    if content is None:
        return

    soup = BeautifulSoup(content, 'html.parser')

    # Extract information
    title = extract_title(soup)
    meta_tags = extract_meta_tags(soup)
    links = extract_links(soup, url)
    images = extract_images(soup, url)

    # Print results
    print("\nTitle:")
    print(title)

    print("\nMeta Tags:")
    for name, content in meta_tags.items():
        print(f"{name}: {content}")

    print("\nLinks:")
    for link in links:
        print(link)

    print("\nImages:")
    for img in images:
        print(f"URL: {img['url']}, Alt Text: {img['alt']}")

if __name__ == '__main__':
    main()


