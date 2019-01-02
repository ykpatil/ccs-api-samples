import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Get the Access Token and used it for the further API calls.
def getToken():
	urlToken = "https://<hostname>:<port number>/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&username=<user name>&password=<password>"
	headers = {
    	'Content-Type': "application/json",
    }

	responseToken = requests.request("POST", urlToken, data=payload, headers=headers, verify=False)
	tokenDict = responseToken.json()
	token = tokenDict['access_token']
	refreshToken = tokenDict['refresh_token']
	return token

url = "https://<hostname>:<port number>/ccs/api/v1/AssetGroup"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()

headers = {
    'Authorization': bearertoken
    }

# Simple Search
querystring = {"Attributes":"(displayName = All DB2 *)"}

# Advanced Search
#querystring = {"Attributes":"(displayName = *)","ContainerPath":"Asset system","SearchSubTree":"True"}

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

GroupData = response.json()

print(response.text)