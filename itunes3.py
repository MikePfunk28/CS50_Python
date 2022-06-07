import json
import sys
import requests

# if users does not enter anything exit
if len(sys.argv) != 2:
    sys.exit()
# users enters name of band they want information on the first 50 songs in apple itunes DB
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# prints title of songs 50 defined by limit
artist_info = response.json()
for result in artist_info["results"]:
    print(result["trackName"])