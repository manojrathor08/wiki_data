import requests
url_retrieve = "https://localhost:8000/retrieve/"

# Make a Get request to retrieve the dataset
response = requests.get(url_retrieve)

# Check the response status code
if response.status_code==200:
  # Parse the Json response into a Pthon object(the dataset)
  dataset = response.json()
  print('Dataset retrieved sucessfully')
  print(dataset)
else:
  print('Failed to retrieve the dataset. Status code:{response.status_code})
