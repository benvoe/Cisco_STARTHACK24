import requests
import json

# defining the api-endpoint  
API_ENDPOINT = "https://webexapis.com/v1/messages"
  
# your access token
ACCESS_TOKEN = "YTQ0M2Y3ZTEtMTY3Ni00MDk2LTlhNTktMGMwMTM1ODM5ZmM1YWQ2Yzk5MmEtZDZm_PE93_6b68d305-fbad-4d67-8d3d-6414c9902447"
  
# headers
HEADERS = {
    'Authorization': 'Bearer ' + "YTQ0M2Y3ZTEtMTY3Ni00MDk2LTlhNTktMGMwMTM1ODM5ZmM1YWQ2Yzk5MmEtZDZm_PE93_6b68d305-fbad-4d67-8d3d-6414c9902447", 
    'Content-Type': 'application/json'
}

def send_meeting_suggestion(user1, user2): 
    # defining a message with card attachment
    with open('webexAPI/message.json') as f:
        DATA = json.load(f)
    # send POST request
    response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(DATA))
    