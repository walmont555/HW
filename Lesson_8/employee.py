import requests


class Company:
    def __init__(self, url):
        self.url = url
    def create_company(self, token, body):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()["id"]