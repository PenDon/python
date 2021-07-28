import requests

headers = {
    "Content-Type": "application/json",
    "Host": "ieeexplore.ieee.org",
    "Origin": "https://ieeexplore.ieee.org",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"
}

data = {
    "highlight": "true",
    "matchPubs": "true",
    "pageNumber": "3",
    "queryText": "image processing",
    "ranges": ["2010_2021_Year"],
    "refinements": ["ContentType:Standards"],
    "returnFacets": ["ALL"],
    "returnType": "SEARCH"
}

url = 'https://ieeexplore.ieee.org/rest/search'
IEEE_response = requests.post(url=url, json=data, headers=headers)
print(IEEE_response.text)
