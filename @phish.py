import requests
from bs4 import BeautifulSoup
import getpass

def phish_login(url, username, password):
    # Send a GET request to the login page
    response = requests.get(url)
    
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        page_content = response.content
        
        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(page_content, 'html.parser')
        
        # Find the login form
        login_form = soup.find('form')
        
        # If a login form is found
        if login_form:
            # Get the input fields of the form
            input_fields = login_form.find_all('input')
            
            # Initialize the data dictionary
            data = {}
            
            # Iterate over the input fields
            for field in input_fields:
                # Get the name and value of the field
                name = field.get('name')
                value = field.get('value')
                
                # If the field is the username or password field
                if name == 'username' or name == 'password':
                    # Prompt the user for the input
                    if name == 'username':
                        user = input("Enter your username: ")
                    elif name == 'password':
                        passw = getpass.getpass("Enter your password: ")
                    
                    # Add the input to the data dictionary
                    data[name] = user if name == 'username' else passw
            
            # Send a POST request with the input data
            response = requests.post(url, data=data)
            
            # If the POST request is successful, the status code will be 200
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
        else:
            return []
    else:
        return []

# Main function
def main():
    # URL of the login page to phish
    url = "http://www.facebook.com/login"
    
    # Username and password
    username = "admin"
    password = "password"
    
    # Phish the login page
    links = phish_login(url, username, password)
    
    # Print the links
    for link in links:
        print(link)

if __name__ == "__main__":
    main()
