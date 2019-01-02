import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
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

url = "https://<hostname>:<port number>/ccs/api/v1/Standards"

querystring = {"attributes":"displayName Contains apache,symc-Standard-TargetTypeIDs=97546792-56b0-4020-9d88-f8786371f2d9", "ContainerPath":"standards\\predefined\\unix",
"Searchsubtree":"true"}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
print("\n Bearer Token is:\n")
print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

print(response.text)
print(response.json)
