import json

import requests
import execjs

# acquire two urls of png
secret_url = 'https://api.bilibili.com/x/web-interface/nav'

response = requests.get(secret_url).json().get('data').get('wbi_img')
# the two png urls
img_url = response.get('img_url')
sub_url = response.get('sub_url')

# two fixed keys in space.5d1dc59f77af79df4138ffd8c0d799245219c122.js
img_key = "4a1d4479a1ea4146bc7552eea71c28e9"
sub_key = "fa5812e23a204d10b332dc24d992432d"
# user's mid
mid = ''

# open the file to encrypt msg
js_file = open('user_info_decode.js','r',encoding='utf8')
# ua
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.0.0'
}

# encrypt msg
js_result_json = json.loads(json.dumps(execjs.compile(js_file.read()).call('encWbi',mid, img_url, sub_url, img_key, sub_key)))
# encrypted result
w_rid = js_result_json.get('w_rid')
wts = js_result_json.get('wts')

# the api url
user_url = f'https://api.bilibili.com/x/space/wbi/acc/info?mid={mid}&token=&platform=web&web_location=1550101&w_rid={w_rid}&wts={wts}'
print(user_url)
# result
print(requests.get(user_url, headers=headers).text)