import json
from pathlib import Path
from typing import Any
def ensure_file(path: Path, default):
 path.parent.mkdir(parents=True, exist_ok=True)
 if not path.exists():
    with open(path, "w", encoding="utf-8") as f:
        json.dump(default, f, indent=2)
def load_json(path: Path, default):
    ensure_file(path, default)
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
 # if file was corrupted, overwrite with default
            with open(path, "w", encoding="utf-8") as fw:
                json.dump(default, fw, indent=2)
            return default
def save_json(path: Path, data: Any):
 path.parent.mkdir(parents=True, exist_ok=True)
 with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)