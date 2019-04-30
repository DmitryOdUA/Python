import json
import os
import xmltodict
import re


def convert_xml_to_dict(file):
    with open(file) as _file:
        content = _file.read()
    return xmltodict.parse(content)


def convert_dict_to_json_file(dict, json_file_path: str):
    dir_path = re.sub(r"/[^/]+\.json", "", json_file_path)
    print(dir_path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    dump = json.dumps(dict, indent=2)
    with open(json_file_path, 'w') as f:
        f.write(dump)
