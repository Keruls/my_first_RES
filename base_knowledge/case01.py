import json
a = [8,4,7,6,9,1,7,4,4,0,1,5]
b = [5,4,2,9,8,8,7,1,0,2,2,4,7,7]

def combine():
    c = []

tup1=[('d',2),('a',1),('b',3),('g','ppp')]

str1 = {'a': '44456df', 'b': '{\n"a":"1111",\n"b":123\n}'}
for i in str1.keys():
    try:
        str1[i] = json.loads(str1.get(i))
    except json.decoder.JSONDecodeError as e:
        print('not json string')
print(str1)