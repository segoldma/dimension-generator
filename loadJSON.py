import json

def load_json(file_path):
    """
    Load the JSON data from the specified file path.
    """
    with open(file_path, 'r') as file:
        return json.load(file)
