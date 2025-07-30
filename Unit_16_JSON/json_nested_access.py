# json Nested access

import json

# Sample nested json

data = {
    "user": {
        "name": "c0ff33py",
        "skills": ["Python", "SQL", "Git"]
    }
}

# Access nested values
print("First skill:", data["user"]["skills"][0])

# Comment: Use chained keys to access nested levels
