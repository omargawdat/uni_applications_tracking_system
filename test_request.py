import requests

url = "https://homeservices.eramapps.com/api/v1/cart-items/680/"

payload = {'package_allocation': '120',
           'problem_description': 'test12232s4543',
           'date': '2024-12-27'}
files = [
    ('problem_image', ('test.jpg', open('test.jpg', 'rb'), 'application/octet-stream'))
]
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMyNjE4NjYzLCJpYXQiOjE3MzI2MTY4NjMsImp0aSI6ImJmZGYxM2FhYjRjMjRjMWZhNzI0M2MyYWFjZGEyZTQ1IiwidXNlcl9pZCI6OX0.8IDxbfU_kJdgX4B_1j9VvQG8nunvCmcQPkYfz33IMXs'
}

response = requests.request("PATCH", url, headers=headers, data=payload, files=files)

print(response.text)
