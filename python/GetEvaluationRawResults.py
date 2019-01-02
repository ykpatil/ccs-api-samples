import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def getToken():
urlToken = "https://ch-ccs:12431/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&username=<domain>\\<user name>&password=password"
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
url = "https://ch-ccs:12431/ccs/api/v1/Results"

payload = "{\"assetid\" : \"7ca3a38e-1e51-42ef-8b5d-88813eae0c14\", \"standardid\" : \"6b020d29-5fe8-47d0-bd89-ccd3339a5ebe\", \"jobrunid\" : \"cae05ae3-8454-43a9-9139-f678b66decf7\"}"


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

bearertoken = "Bearer " + getToken()
print("\n Bearer Token is:\n")
print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }

response = requests.request("POST", url, data=payload, headers=headers, verify=False)

print(response.text)
print(response.json)