import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def getToken():
	urlToken = "https://<host name>:<port number>/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&username=<domain name>\\<user name>&password=<password>"
	headers = {
    	'Content-Type': "application/json",
    }

	responseToken = requests.request("POST", urlToken, data=payload, headers=headers, verify=False)

	tokenDict = responseToken.json()
	token = tokenDict['access_token']
	refreshToken = tokenDict['refresh_token']
	#print("bearer Token is:\n")
	#print(token)
	#print("\n Refresh Token is:\n")
	#print(refreshToken)
	return token

url = "https://<host name>:<port number>/ccs/api/v1/AssetGroup/4b800e8a-c778-41e7-8bf3-37dc2f5284f6/Assets"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
#print("\n Bearer Token is:\n")
#print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken,
    'Content-Type': "application/json"
    }

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)
print(response.json)