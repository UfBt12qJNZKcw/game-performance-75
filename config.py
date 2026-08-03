import os

class Config:
    def __init__(self):
        self.debug = self.get_env_variable('DEBUG', default='False') == 'True'
        self.db_url = self.get_env_variable('DATABASE_URL', default='sqlite:///default.db')
        self.api_key = self.get_env_variable('API_KEY')

    @staticmethod
    def get_env_variable(var_name, default=None):
        return os.environ.get(var_name, default)

    def load(self):
        return {
            'debug': self.debug,
            'db_url': self.db_url,
            'api_key': self.api_key
        }

config = Config().load()