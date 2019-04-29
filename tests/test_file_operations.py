import json
import os

from utils import collection_utils
from utils import file_utils

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_DATA_PATH = SCRIPT_DIR + "/../samples/xml/test_data.xml"
OUTPUT_DIR = SCRIPT_DIR + "/../samples/json"
UPDATED_FILE_PATH = OUTPUT_DIR + "/updated_test_data.json"


def test_file_exists():
    assert os.path.exists(TEST_DATA_PATH)


def test_loaded_from_xml_data():
    actual_data = file_utils.convert_xml_to_dict(TEST_DATA_PATH)
    assert actual_data.get("PERSONS").get("PERSON")[0].get("FIRST_NAME") == "Lector"


def test_fields_updated():
    actual_data = file_utils.convert_xml_to_dict(TEST_DATA_PATH)
    collection_utils.recursive_search_and_update_value(actual_data, "YOUR", "THIS_VALUE_WAS_REPLACED")
    assert actual_data.get("PERSONS").get("PERSON")[1].get("FIRST_NAME") == "THIS_VALUE_WAS_REPLACED"


def test_json_file_created():
    dict_from_xml = file_utils.convert_xml_to_dict(TEST_DATA_PATH)
    collection_utils.recursive_search_and_update_value(dict_from_xml, "YOUR_FIRST_NAME", "THIS_VALUE_WAS_REPLACED")
    file_utils.convert_dict_to_json_file(dict_from_xml, UPDATED_FILE_PATH)
    assert os.path.exists(UPDATED_FILE_PATH)


def test_json_file_content():
    dict_from_xml = file_utils.convert_xml_to_dict(TEST_DATA_PATH)
    collection_utils.recursive_search_and_update_value(dict_from_xml, "YOUR", "THIS_VALUE_WAS_REPLACED")
    file_utils.convert_dict_to_json_file(dict_from_xml, UPDATED_FILE_PATH)
    with open(UPDATED_FILE_PATH, "r") as read_it:
        actual_data = json.load(read_it)
    assert actual_data.get("PERSONS").get("PERSON")[1].get("FIRST_NAME") == "THIS_VALUE_WAS_REPLACED"
