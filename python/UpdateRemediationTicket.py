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
	print("bearer Token is:\n")
	print(token)
	print("\n Refresh Token is:\n")
	print(refreshToken)
	return token

url = "https://<hostname>:<port number>/ccs/api/v1/remediationtickets/"

payload = " {\"TicketNumber\":\"INCA0000001\",\"ticketDescription\":\"AzadDescriptionjks\",\"Priority\":\"MyP\",\"AssignedTo\":\"AzadRai\", \"TicketState\":\"4\"}"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()

headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }

response = requests.request("PATCH", url, data=payload, headers=headers, verify=False)

print(response.text)
print(response.json)
