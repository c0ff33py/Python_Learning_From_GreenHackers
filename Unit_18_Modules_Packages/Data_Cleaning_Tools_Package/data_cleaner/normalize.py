# normalize.py
def strip_spaces(data_list):
    """Remove leading/ trailing spaces from strings"""
    return [item.strip() if isinstance(item, str) else item for item in data_list]

def to_lowercase(data_list):
    """Convet all strings in list to lowercase"""
    return [item.lower() if isinstance(item, str) else item for item in data_list]