import requests

api_url = "https://restful-booker.herokuapp.com/booking/1"
booking = {"firstname": "Tomasz", "lastname": "Nowak", "totalprice": 222, "depositpaid": False, "bookingdates": {"checkin": "2021-12-28", "checkout": "2021-12-31"}}
response = requests.put(api_url, json=booking, headers={'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
# print(response.json())
print(response.status_code)
