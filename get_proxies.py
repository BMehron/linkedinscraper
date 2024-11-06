import requests

# url = 'https://ipv4.icanhazip.com'
# proxy = 'geo.iproyal.com:12321'
# proxy_auth = 'itOAmhhZijdF0sUI:Z9R4HTz0r2u5x0zb_country-ch,fr_session-5oggDA58_lifetime-30m_streaming-1'
# proxies = {
#     'http': f'http://{proxy_auth}@{proxy}',
#     'https': f'http://{proxy_auth}@{proxy}'
# }

# response = requests.get(url, proxies=proxies)
# print(response.text)

import requests

api_token = '171151fce956bfd96fccb6ab25ff77da8226cbea08b1775e59de057349de'

url = 'https://resi-api.iproyal.com/v1/access/generate-proxy-list'

data = {
    'format': '{hostname}:{port}:{username}:{password}',
    'hostname': 'example.hostname.com',
    'port': 1234,
    'rotation': 'sticky',
    'location': '_country-sg',
    'proxy_count': 10,
    'subuser_hash': 'example_subuser_hash'
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

response = requests.post(url, json=data, headers=headers)

print(response.text)


Hello,

I'm trying to use your API in order to get proxy list automatically. I'm using your code from documentation, paragraph: Generate Proxy List. The code is following 

import requests

api_token = '<your_api_token>'
url = 'https://resi-api.iproyal.com/v1/access/generate-proxy-list'

data = {
    'format': '{hostname}:{port}:{username}:{password}',
    'hostname': 'example.hostname.com',
    'port': 1234,
    'rotation': 'sticky',
    'location': '_country-sg',
    'proxy_count': 10,
    'subuser_hash': 'example_subuser_hash'
}

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_token}'
}

response = requests.post(url, json=data, headers=headers)

print(response.text)
