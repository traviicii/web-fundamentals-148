import requests
from bs4 import BeautifulSoup

# Fetching data from a website -- Ex. Coding Temple Website

# Create a response object
response = requests.get('https://www.codingtemple.com/')

# Check the status of our request respobnse (using the status_code attribute)
print(response.status_code)

print(response.content) #<--- this is just printing the entire contents of the response object. Not very nice looking

# Use beautilfu Soup to organize this information (Parse the HTML)

soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.prettify()) # Formats the html object into a prettier more readable format

# Using beautiful soup to access specific elements

print(soup.title.text)

print(soup.a)

print(soup.h1.text)