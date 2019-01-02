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

url = "https://<hostname>:<port number>/ccs/api/v1/Jobs/<JobID>/jobruns"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

querystring = {"count":"1"}

bearertoken = "Bearer " + getToken()
print("\n Bearer Token is:\n")
print(bearertoken + "\n")

headers = {
    'Authorization': bearertoken
    }

response = requests.request("GET", url, headers=headers, params=querystring, verify=False)

print(response.text)