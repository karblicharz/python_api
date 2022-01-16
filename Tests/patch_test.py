import requests

api_url = "https://restful-booker.herokuapp.com/booking/1"
booking = {"firstname": "Emil", "lastname": "Nowak", "totalprice": 555, "depositpaid": True}
request = requests.patch(api_url, json=booking, headers={'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
print(request.status_code)
print(request.json())
