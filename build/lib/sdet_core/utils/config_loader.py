# src/sdet_core/utils/config_loader.py
import yaml
import os
from pathlib import Path

class ConfigLoader:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config_data = self._load_file()

    def _load_file(self):
        if not Path(self.config_path).exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {self.config_path}")
        
        with open(self.config_path, 'r') as file:
            return yaml.safe_load(file)

    def get_base_url(self):
        # Permite trocar o ambiente via variável de sistema ou usar o default do YAML
        env = os.getenv("TEST_ENV", self.config_data.get("current_env", "dev"))
        return self.config_data["environments"][env]["base_url"]

    def get_value(self, key, default=None):
        return self.config_data.get("default", {}).get(key, default)