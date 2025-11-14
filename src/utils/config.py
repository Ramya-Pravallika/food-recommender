import yaml
from pathlib import Path


_config_cache = None
CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.yaml"


def load_config():
global _config_cache
if _config_cache is None:
with open(CONFIG_PATH, "r") as f:
_config_cache = yaml.safe_load(f)
return _config_cache
