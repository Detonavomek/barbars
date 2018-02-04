from .config import ConfigManager


class Bot:

    def __init__(self, config):
        self.config = config

    def start(self):
        print(ConfigManager(self.config).generate_config())
