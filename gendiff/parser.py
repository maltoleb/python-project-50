import json

import yaml

from pathlib import Path


def parse(file_path):
    file_path = Path(file_path)
    extension = file_path.suffix.lower()
    with open(file_path) as f:
        if extension == '.json':
            return json.load(f)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(f)