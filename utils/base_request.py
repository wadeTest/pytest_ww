import sys

sys.path.extend(["d:\\pytest_ww"])
import requests


class HTTPRequest:
    headers = {"Content-Type": "application/json"}

    def __init__(self, base_url):
        self.base_url = base_url
        print(f"這是BASE URL：{base_url}")
        self.session = requests.session()

    def get(self, path=None):
        res = self.session.get(f"{self.base_url}{path}", headers=self.headers)
        return res

    def post(self, path, data=None, json=None):
        print(f"收到的URL＿:{self.base_url}{path}")
        res = self.session.post(
            f"{self.base_url}{path}", headers=self.headers, data=data, json=json
        )
        return res
