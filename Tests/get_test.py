import requests

api_url = "https://restful-booker.herokuapp.com/booking/2"
response = requests.get(api_url)
print(response.status_code)
print(response.json())

