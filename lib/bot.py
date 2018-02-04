from .connector import Connector
from .parser import Parser


class Bot:

    def __init__(self):
        self.connector = Connector()
        self.parser = Parser()
        self.config = None

    def load(self, config):
        self.config = config

    def auth(self):
        auth_result = self.connector.auth(self.config)
        self.parser.auth(auth_result)
        raise NotImplementedError
