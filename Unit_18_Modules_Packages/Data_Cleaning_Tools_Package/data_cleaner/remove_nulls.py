# remove_nulls.py

def remove_none(data_list):
    """Remove None vales from a list"""
    return [item for item in data_list if item is not None]

def remove_empty_strings(data_list):
    """Remove empty strings from a list"""
    return [item for item in data_list if item != ""]

