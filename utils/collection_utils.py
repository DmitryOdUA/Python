from collections import OrderedDict


def recursive_search_and_update_value(collection, value_to_search: str, replace_with: str):
    if type(collection) is OrderedDict:
        collection: OrderedDict
        keys = collection.keys()
        for key in keys:
            value = collection.get(key)
            if type(value) is str:
                if value_to_search in value:
                    collection.update({key: replace_with})
            else:
                recursive_search_and_update_value(value, value_to_search, replace_with)
    elif type(collection) is list:
        for item in collection:
            recursive_search_and_update_value(item, value_to_search, replace_with)
    else:
        raise ValueError("incorrect type of data: " + str(type(collection)))
