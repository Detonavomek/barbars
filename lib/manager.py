from .config import ConfigManager
from .bot import Bot


class BotManager:

    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None
        self.bot = Bot()

    def start(self):
        self.config = ConfigManager(self.config_path).generate_config()
        self.bot.load(self.config)

        self.bot.auth()
