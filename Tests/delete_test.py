import requests

api_url = "https://restful-booker.herokuapp.com/booking/1"
request = requests.delete(api_url, headers={'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM='})
print(request.status_code)

