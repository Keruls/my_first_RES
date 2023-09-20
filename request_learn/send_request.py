import requests

class c1:
    @classmethod
    def fun(cls):
        l = {'url': 'http://127.0.0.1:9999/api/sys/login',
             'headers': {'Content-Type': 'application/json'},
             'json': {'mobile': '13800000001', 'password': '123456'}}
        res = requests.post(url=l['url'],
                            json=l['json'],
                            headers = l['headers'],
                            proxies = {'http': 'http://127.0.0.1:8888', 'https': 'http://127.0.0.1:8888'})
        return res

    @classmethod
    def fun_main(cls):
        return cls.fun()

res = c1.fun()
print(res.text)