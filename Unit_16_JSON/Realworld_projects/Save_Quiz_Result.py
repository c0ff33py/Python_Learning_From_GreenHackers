# Goal: Ask 1-2 questions . Store result in results.json

import json
import os
from datetime import datetime

filename = "results.json"
if os.path.exists(filename):
    with open(filename, "r") as f:
        results = json.load(f)

else:
    results = []

# Simple quiz
answer = input("Q: what is 2 + 2?: ")
correct = answer == "4"

# Add result
results.append({
    "timestamp": str(datetime.now()),
    "question": "2 + 2",
    "user_answer": answer,
    "correct": correct
})

# Save
with open(filename, "w") as f:
    json.dump(results, f, indent=2)

print("Quiz result recorded.")
