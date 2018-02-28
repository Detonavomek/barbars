import json


class Config:
    def __init__(self, config_json):
        self.name = config_json.get('name')
        self.username = config_json.get('username')
        self.password = config_json.get('password')

    def __str__(self):
        return f'{self.name}'


class ConfigManager:

    def __init__(self, path_to_config):
        with open(path_to_config, 'r') as f:
            self.config_json = json.load(f)

    def generate_config(self):
        return Config(self.config_json)
