# 2018-12-07 web service

import json

data = '''
{
    "name" : "Chuck",
    "phone": {
        "type" : "inil",
        "number" : "+1 734 303"
    },
    "email" : {
        "hide": "yse"
    }
}
'''

info = json.loads(data)
print('Name: ', info['name'])
print('Hide: ', info["email"]["hide"])
