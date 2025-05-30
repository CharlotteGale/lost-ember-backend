import json
import os

def load_lineages():
    file_path = os.path.join(os.path.dirname(__file__), 'lineages.json')
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)