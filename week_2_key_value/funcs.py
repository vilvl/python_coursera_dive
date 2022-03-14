import tempfile
import os
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_json_data():
    if not os.path.exists(storage_path):
        return None 

    with open(storage_path, 'r', encoding='utf8') as f:
        return json.load(f)

def show_by_key(key):
    json_data = get_json_data()
    if json_data and key in json_data:
        print(', '.join(json_data[key]))
    else: print(r'## No data ##')

def store_by_key(key, value):
    json_data = get_json_data()
    if not json_data:
        json_data = {key: [value,]}
    elif key in json_data:
        json_data[key].append(value)
    else:
        json_data[key] = [value,]
    with open(storage_path, 'w+', encoding='utf8') as f:
        json.dump(json_data, f)
