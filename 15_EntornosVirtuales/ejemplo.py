import requests # importing the request module

url = 'https://www.example.com' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.text)