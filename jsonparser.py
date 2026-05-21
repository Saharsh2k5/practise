import json
from pathlib import Path

data = {"tool": "parser", "version": "1.0", "log_level": "INFO"}
Path("config.json").write_text(json.dumps(data, indent=2))

with open("config.json") as f:
    config = json.load(f)

config["version"] = "1.1"

with open("config.json", "w") as f:
    json.dump(config, f, indent=2)