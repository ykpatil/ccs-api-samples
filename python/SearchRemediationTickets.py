# Script to find out all the remediation tickets based on Ticket State and Ticket provider type
# For more details Refer the CCS REST API document at : https://apidocs.symantec.com/home/CCS

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Variable 
# Replace the <hostname> with CCS applicatio server host name
# Replace the <port number> with the configured port number for REST API, Default Port Number : 12431
# Replace the <user name> and <password> with valide CCS user name and password for example: UserName = domain1\\administrator, password = pass@123   
HostName = '<hostname>'
PortNumber = '<port number>'
UserName = '<user name>'
Password = '<password>'

# Function to generate CCS REST API access token
def getToken():
	urlToken = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/oauth/tokens"

	payload = "grant_type=password&username=" + UserName + "&password=" + Password +""
	headers = {
    	'Content-Type': "application/json",    	
    }
	responseToken = requests.request("POST", urlToken, data=payload, headers=headers, verify=False)
	autheticationresult = responseToken.status_code
	if (autheticationresult!=200) :
		print("\nAuthentication Failed. Please check if the REST API is enbaled and User name and password is correct\n")
		exit()
	tokenDict = responseToken.json()
	token = tokenDict['access_token']
	refreshToken = tokenDict['refresh_token']
	print("bearer Token is:\n")
	print(token)
	print("\n Refresh Token is:\n")
	print(refreshToken)
	return token

# Remediation Ticket URI 
url = "https://" + HostName + ":" + PortNumber + "/ccs/api/v1/RemediationTickets"
# Provide the TicketState and TicketProviderType for searcing the ticket details
querystring = {"Fields":"(TicketState=1,TicketProviderType=2)","page":"0","pagesize":"2"}
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
bearertoken = "Bearer " + getToken()
headers = {
    'Authorization': bearertoken ,
    'Content-Type': "application/json"
    }
response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
print(response.text)
print(response.json)
