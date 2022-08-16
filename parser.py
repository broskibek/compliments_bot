import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

list_of_compliments = []

url = 'https://castlots.org/generator-komplimentov-devushke/generate.php'

headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Origin': 'https://castlots.org',
'Referer': 'https://castlots.org/generator-komplimentov-devushke/',
'Accept-Language': 'ru',
'Host': 'castlots.org',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
'Content-Length': '0',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'X-Requested-With': 'XMLHttpRequest'
}

# while 1:
for i in range(150):
        res = requests.get(url, headers = headers, verify = False)
        parsed_text = json.loads(res.text)
        list_of_dict_values = list(parsed_text.values())
        # print(list_of_dict_values[1])
        if list_of_dict_values[1] not in list_of_compliments:
                list_of_compliments.append(list_of_dict_values[1])
                # print(list_of_compliments[i])
        else:
                pass
