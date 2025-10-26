import json
import yaml


def parse(file_path):
    file_path = str(file_path)
    with open(file_path) as f:
        content = f.read()
        extension = file_path.split('.')[-1]
        if extension == 'json':
            return json.loads(content)
        elif extension in ('yml', 'yaml'):
            return yaml.safe_load(content)