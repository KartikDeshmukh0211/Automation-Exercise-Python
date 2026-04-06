from configparser import ConfigParser
import os

class ConfigReader:
    def __init__(self):
        config = ConfigParser()

        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "configs",
            "config.ini"
        )

        config.read(config_path)
        self.config = config

    def get_base_url(self):
        return self.config.get("DEFAULT", "base_url")

    # def get_browser(self):
    #     return self.config.get("DEFAULT", "browser")

    # def get_timeout(self):
    #     return self.config.getint("DEFAULT", "timeout")

    def get_email(self):
        return self.config.get("LOGIN", "email")

    def get_password(self):
        return self.config.get("LOGIN", "password")