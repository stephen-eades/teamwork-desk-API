# teamwork-desk-API
Script template that can be used for automating support/ticketing processes utilizing the available Teamwork Desk API

## Overview
This python template has the initial code for performing GET requests that can be used to gather information from your companies Teamwork desk inboxes. The full API documentation is available at http://developer.teamwork.com/desk/  
  
For support email desk@teamwork.com  

## Setup
* Must have Python installed: check with `Python --version` in your terminal.  
* It's best to run this with Python 3; but Python 2 should be ok.
* Assumes user has PIP (see https://pip.pypa.io/en/stable/installing)
* Install Requests library `pip install requests`
* Install Urllib3 `pip install urllib3`

## Usage
Within the PARAMETERS section:  
* Add your company name seen in your Teamwork Desk url such as: https://COMPANY.teamwork.com/desk/...  
* Add your generated Teamwork Desk API key. See more here: https://support.teamwork.com/desk/my-profile/generating-an-api-key  
* Add the endpoint you'd like to take action on. See Teamworks reference here: https://deskdeveloper.teamwork.com/
   
Within the GET REQUEST section:  
* Formats your call and provides a response status message
* If successful, it will output the headers
  
Within the CONSUME REQUEST section:   
* Outputs the data in json format using our imported Pretty Print module.
