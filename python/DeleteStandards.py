import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def getToken():
	urlToken = "https://<host name>:<port number>/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&amp;username=<domain name>\\<user name>&password=<password>"
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

url = "https://<host name>:<port number>/ccs/api/v1/Standards"
payload = "{\"StandardList\":[{\"Type\":\"Name\",\"Standards\":[\"Test Standard for AIX\",\"Test Windows 2012\"]},{\"Type\":\"ID\",\"Standards\":[\"77fd3e2e4e7e1800-3775-4ba8-9b9d-37d16cccd5a7\",\"3a9abc89-ae28-46ec-ab6f-0885e40e90e1\",\"78d3c003-5f02-4d39-82b8-a90a8613167c\"]}],\"ContainerPath\":\"standards\",\"DeletePredefinedStandard\":\"false\"}"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
#print("\n Bearer Token is:\n")
#print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }

response = requests.request("DELETE", url, data=payload, headers=headers, verify=False)

print(response.text)
print(response.json)
