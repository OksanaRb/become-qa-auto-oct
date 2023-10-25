import json
import os
from typing import Any


class DictConfigProvider():

    def __init__(self, input_values: dict) -> None:
        super().__init__()
        self.values = input_values

    def get(self, item_name: str) -> Any:
        return self.values[item_name]


class OSConfigProvider():
    @staticmethod
    def get(item_name: str) -> Any:
        value = os.getenv(item_name)
        return value


class JSONConfigProvider():
    @staticmethod
    def _read_config(config_path):
        with open(config_path) as json_file:
            return json.load(json_file)

    @staticmethod
    def get(item_name: str) -> Any:
        value = JSONConfigProvider._read_config(
            "/framework/envs_config/dev.json"
        )
        return value.get(item_name)


class Config:
    """
    Holds all the settings of your framevork
    """

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers

        self.conf_dict = {}
        self._register("BASE_URL_API")
        self._register("BASE_URL_UI")

    

    def get(self, item_name: str) -> Any:
        return self.conf_dict:
        if item not in self.conf_dict:
            raise AttributeError(f"Please register '{item} var before usage")

            return self.conf_dict[item]

    def _register(self, item_name: str) -> None: 
        # BASE_URL_API
        for provider in self.config_providers:
            value = provider.get(item_name)
            if value is not None:
                self.conf_dict[item_name] = value
                return

        raise ValueError(f{item_name} name is missing in config providers)


dict_confprovider = DictConfigProvider({
    'BROWSER' : 'chrome',
    'SELENIUM_GRID_URL' : 'http://172.19.0.2:4444/wd/hub', # 0.0.0.0 --> selenium-hub
    })

config = Config([OSConfigProvider, JSONConfigProvider, dict_confprovider])