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

# defining a message with card attachment
f = open('message.json')
DATA = json.load(f)
f.close()

payload = {
  "roomId": "Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYzFlMzVhODAtZTc3MC0xMWVlLWE4MDUtYzUwMzEwMmJkODBi",
  "text": "PROJECT UPDATE - A new project plan has been published on Box: http://box.com/s/lf5vj. The PM for this project is Mike C. and the Engineering Manager is Jane W.",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
          {
            "type": "TextBlock",
            "text": "Adaptive Cards",
            "size": "large"
          }
        ],
        "actions": [
          {
            "type": "Action.OpenUrl",
            "url": "http://adaptivecards.io",
            "title": "Learn More"
          }
        ]
      }
    }
  ]
}
         
# send POST request
response = requests.post(API_ENDPOINT, headers=HEADERS, data=json.dumps(DATA)) 
  
# extracting response text  
print(response.text)  