import json
from datetime import datetime
import requests

# Get today's date and assign your api_key to the variable api_key
date = datetime.today().strftime('%Y-%m-%d')
api_key = 'apiKey=yourApiKey'  # Flag 1

# API endpoint
api_endpoint = 'https://newsapi.org/v2/'

# Main endpoints
headlines_endpoint = 'top-headlines?'
everything_endpoint = 'everything?' 

"""

To know all the parameters available: - https://newsapi.org/docs/endpoints -

"""

def get_url(api_endpoint, main_endpoint, api_key, **kwargs):
    """Returns a full URL. **kwargs will be the parameters chosen"""
    url = f"{api_endpoint}{main_endpoint}{api_key}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"
    
    return url

# Decorator function
def exceptions(func):
    def wrapper():
        func()

        if func():
            file = f'{date}.json'

            with open(file) as f:
                data = json.load(f)
                f.close()          

            return data

        else:
            print("Request failed. Please try again later.")
            return

    return wrapper

@exceptions
def main():
    while True:    
        url = get_url(api_endpoint, headlines_endpoint, api_key, country='gb')

        # HTTP request and transform the object to json if status_code=200
        r = requests.get(url)
        status_code = r.status_code

        if str(status_code) == '200':
            r_json = r.json()        

            # Delete unwanted data
            for article in r_json['articles']:
                del article['source']
                del article['author']
                del article['urlToImage']
                del article['content']
                del article['publishedAt']
                del article['description']

            # Create a .json file with today's date to store the data from the r_json variable.
            # 'w' will override previous news if program is run twice in the same day
            with open(f"{date}.json", 'w') as f:
                json.dump(r_json['articles'], f)
                f.close()
                
            return True
            break
        
        else:
            return False
            break

# Runs the main function and assigns the .json file output to variable data
data = main()

# Formats the data into one single string, easily readable on the email
data_as_string = ""

for article in data:
    for key, value in article.items():
        if key == 'title':
            data_as_string += f"{value}\n"
        else:
            data_as_string += f"{value}\n\n"
