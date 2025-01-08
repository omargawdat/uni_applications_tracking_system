import json

import requests

url = "https://accept.paymob.com/api/ecommerce/orders/transaction_inquiry"

payload = json.dumps({
    "order_id": "250121124"
})
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token egy_sk_test_1cb4ddc00c87c0c981a9a12dc71c1bac3f9c615d454b169342a4f700039d5993'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
