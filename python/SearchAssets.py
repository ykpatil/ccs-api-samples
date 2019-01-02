import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Get the Access Token and use it for the further API calls.
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

url = "https://<hostname>:<port number>/ccs/api/v1/Assets"

## Simple Search
#querystring = {"attributes":"displayname Contains 10.211.64"}

## Advanced Search
querystring = {"attributes":"(symc-csm-AssetSystem-Asset-unix-Machine-OSSystem Contains linux, displayname Contains 10.211.64)","ContainerPath":"asset system",
"searchsubtree":"false","page":"0","pagesize":"1"}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()

headers = {
    'Authorization': bearertoken
    }

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

assetsData = response.json()
print(response.text)