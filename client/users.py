import requests

class Users:
    base_url = 'http://localhost:5000/users'

    def get_users(self):
        return requests.get(self.base_url).json()

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.base_url}/{user_id}").json()

    def criar_user(self, user):
        return requests.post(self.base_url, json = user).json()