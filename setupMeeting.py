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
DATA = {
    'roomId': 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vODE2ODMyYTAtZTc3YS0xMWVlLThkNWUtZmY4ODlkMjA1MjNj',
    'text': ' ',
     "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "type": "AdaptiveCard",
        "version": "1.3",
        "body": [
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "items": [
                  {
                    "type": "Image",
                    "url": "https://cdn0.iconfinder.com/data/icons/users-groups-1/512/user_group_two-512.png",
                    "size": "Medium",
                    "height": "50px"
                  }
                ],
                "width": "auto"
              },
              {
                "type": "Column",
                "items": [
                  {
                    "type": "TextBlock",
                    "text": "Connect to people",
                    "weight": "Lighter",
                    "color": "Accent"
                  },
                  {
                    "type": "TextBlock",
                    "weight": "Bolder",
                    "text": "Meeting Recommendation",
                    "horizontalAlignment": "Left",
                    "wrap": true,
                    "color": "Light",
                    "size": "Large",
                    "spacing": "Small"
                  }
                ],
                "width": "stretch"
              }
            ]
          },
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": 35,
                "items": [
                  {
                    "type": "TextBlock",
                    "text": "Date suggestion:",
                    "color": "Light"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Meeting Partner",
                    "weight": "Lighter",
                    "color": "Light",
                    "spacing": "Small"
                  }
                ]
              },
              {
                "type": "Column",
                "width": 65,
                "items": [
                  {
                    "type": "TextBlock",
                    "text": "Mar 22, 2024",
                    "color": "Light"
                  },
                  {
                    "type": "TextBlock",
                    "text": "Leon Bernard | Design",
                    "color": "Light",
                    "weight": "Lighter",
                    "spacing": "Small"
                  }
                ]
              }
            ],
            "spacing": "Padding",
            "horizontalAlignment": "Center"
          },
          {
            "type": "TextBlock",
            "text": "We're making it easier for you to connect with new people and exchange interesting ideas to further develop projects and products. ",
            "wrap": true
          },
          {
            "type": "TextBlock",
            "text": "Learn more:"
          },
          {
            "type": "ColumnSet",
            "columns": [
              {
                "type": "Column",
                "width": "24px",
                "items": [
                  {
                    "type": "Image",
                    "altText": "",
                    "url": "https://static.vecteezy.com/system/resources/previews/000/442/525/non_2x/vector-chat-icon.jpg",
                    "size": "Small",
                    "width": "23px"
                  }
                ],
                "spacing": "Small"
              },
              {
                "type": "Column",
                "width": "auto",
                "items": [
                  {
                    "type": "TextBlock",
                    "text": "[Make an appointment with Leon]()",
                    "horizontalAlignment": "Left",
                    "size": "Medium",
                    "color": "Accent"
                  }
                ],
                "verticalContentAlignment": "Center",
                "horizontalAlignment": "Left",
                "spacing": "Small"
              }
            ]
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