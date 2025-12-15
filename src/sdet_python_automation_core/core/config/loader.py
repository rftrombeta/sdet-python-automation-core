import yaml
from pathlib import Path


class ConfigLoader:
    """
    Responsável por carregar configurações externas (YAML)
    para o Automation Core.
    """

    def __init__(self, config_path: str = None):
        """
        :param config_path: caminho opcional para o arquivo yaml
        """
        if config_path:
            self.config_path = Path(config_path)
        else:
            self.config_path = Path.cwd() / "configs" / "settings.yaml"

    def load(self) -> dict:
        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: {self.config_path}"
            )

        with open(self.config_path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
