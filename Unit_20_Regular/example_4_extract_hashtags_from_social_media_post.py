import re

#example social media post
post = "Learning #Python is fun! Let's build #DataScience and #AI project together. #coding"

#Pattern for hashtags(#word)
pattern = r"#\w+"

# Find all hashtags in the post
hashtags = re.findall(pattern, post)

print("Extracted Hashtags: ")
for tag in hashtags:
    print(tag)