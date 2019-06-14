############ IMPORTS ############
import requests
import time
import json
from pprint import pprint
import certifi
import urllib3 # docs: https://urllib3.readthedocs.io/en/latest/index.html
http = urllib3.PoolManager( # 10 is default, can be increased if needed
    cert_reqs='CERT_REQUIRED', # docs: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
    ca_certs=certifi.where()) 


############ PARAMETERS ############
company = "yourCompany" #
key = "yourKey" # API key
action = "desk/v1/yourEndpoint/" # define endpoint(see: http://deskdeveloper.teamwork.com/desk)


############ GET REQUEST ############
url = "https://{0}.teamwork.com/{1}".format(company, action) # create our URL with defined parameters above
headers = urllib3.util.make_headers(basic_auth=key + ":xxx") # authorize request using basic http auth
request = http.request('GET', url, headers=headers) # make GET request with auth header and URL parameters
response = request.status # capture return value in response

# View status and catch errors
if response == 200:
    print('Success! Status of: ')
    print(response)
elif response == 404:
    print('Not Found. Status of: ')
    print(response)
else:
    print('Error occurred. returned status of: ')
    print(response)

print(request.headers)
print()


############ CONSUME REQUEST ############
binary = request.data
output = json.loads(binary)
pprint(output)
