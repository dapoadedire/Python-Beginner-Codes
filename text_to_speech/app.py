
# ogwctvrrgd-833a-467c-a8ae-0ae82798486a
from email import header
import requests

from credentials import *
api_key = key
endpoint = "https://api.assemblyai.com/v2/transcript/ogwctvrrgd-833a-467c-a8ae-0ae82798486a"

headers = {
    "authorization" : api_key,
}

response = requests.get(endpoint, headers=headers)

print(response.json())