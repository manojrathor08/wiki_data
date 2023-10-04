import requests

# Define the URL for FastAPI application
url = "http://localhost:8000/wiki/"

# Prompt the user to enter a Eikipedia title and length of the summary
title = input("Enter a wikipedia title:")
length = input("Enter the summary length (defual is 10):")

# Define the query parameters
params = {'title': title, 'length':length}
# Make the GET request with the query parameters
repsone = requests.get(url,params = params)
