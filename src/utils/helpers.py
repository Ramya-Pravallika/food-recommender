import json
from pathlib import Path




def ensure_dir(path):
p = Path(path)
if not p.exists():
p.mkdir(parents=True, exist_ok=True)




def save_json(obj, path):
ensure_dir(Path(path).parent)
with open(path, "w") as f:
json.dump(obj, f, indent=2)
