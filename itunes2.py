import json
import sys
import requests

# if users does not enter anything exit
if len(sys.argv) != 2:
    sys.exit()
# users enters name of band they want information on the first song in apple itunes DB
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# formats json file and indents 2 spaces, and lists each key with value
print(json.dumps(response.json(), indent=2))