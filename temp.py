import requests

# Define the request URL
url = "https://api.mapbox.com/search/searchbox/v1/suggest"

# Define the query parameters
params = {
    "q": "مصر الجديدة",
    "access_token": "pk.eyJ1IjoiZXhhbXBsZXMiLCJhIjoiY20zc3d6ZXozMDJrcjJrb2JycmxsOW1vbiJ9.LY7szK0K0hnF0NE3WhVGZw",
    "language": "en",
    "limit": 10,
    "country": "eg",
    "session_token": "05456e44-5420-4611-893a-02447420f12a",
    "proximity": "31.24579219586431,30.010032657613365"
}

# Define the headers to match the request
headers = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://docs.mapbox.com",
    "referer": "https://docs.mapbox.com/",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# Perform the GET request
response = requests.get(url, headers=headers, params=params)

# Output the response
if response.status_code == 200:
    print("Request Successful!")
    print("Response JSON:")
    print(response.json())  # Print the JSON response
else:
    print(f"Request Failed with status code: {response.status_code}")
    print(f"Error: {response.text}")
