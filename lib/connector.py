import requests

from . import constants


class Connector:
    def __init__(self):
        self.session = requests.Session()

    def auth(self, config):
        return self.session.post(constants.AUTH_URL, data={'username': config.username, 'password': config.password})
