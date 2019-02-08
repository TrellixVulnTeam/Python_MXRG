import json


input = '''
[
    { "id" : "001",
      "x" : "2",
      "name" : "Chuck"
    },
    { "id" : "009",
      "x" : "7",
      "name" : "chunck"
    }
]
'''


# json을 리스트로 받아와서 안의 원소를 딕셔너리로 저장
info = json.loads(input)
# list이기 때문에 len 을 사용할 수 있음
print('User count:', len(info))


for item in info:
    print('name: ', item['name'])
    print('id: ', item['id'])
    print('attribute: ', item['x'])