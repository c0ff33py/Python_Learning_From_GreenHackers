# main.py
from data_cleaner import remove_none, remove_empty_strings, strip_spaces, to_lowercase
raw_data = [" Apple", None, "Banana", "","Cherry"," date "]


# Step 1: Remove empty strings
cleaned_data = remove_empty_strings(raw_data)
# Step 2: Remove None values
cleaned_data = remove_none(raw_data)
# Step 3: Strip extra spaces
cleaned_data = strip_spaces(cleaned_data)
# Step 4: Convert to lowercase
cleaned_data = to_lowercase(cleaned_data)

print("Cleaned data: ", cleaned_data)
