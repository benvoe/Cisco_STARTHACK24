# #############################################################################
# Project:   Submission to START Hackathon 2024 - Cisco Challenge
# Team:      BembelEngineers
# Authors:   Kevin Riehl, Leon Bernard, Benedikt Völker
# Date:      March 21st, 2024
# #############################################################################




# #############################################################################
# Imports
# #############################################################################
import requests
import json
import socket
import os
import sys




# #############################################################################
# Methods
# #############################################################################
def authenticate():
    # Gets public key from spaces and places in correct format
    print("-- No API Key Found --")
    # Gets user to paste in generated token from app
    token = input('Enter provided API key here: ')
    # Writes activation key to file. This key can be used to open up Firehose connection
    fileWriter = open("resources/API_KEY.txt", "a")
    fileWriter.write(token)
    fileWriter.close()
    return token

def establishConnection():
    # work around to get IP address on hosts with non resolvable hostnames
    socketObj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketObj.connect(("8.8.8.8", 80))
    IP_ADRRESS = socketObj.getsockname()[0]
    socketObj.close()
    url = 'http://' + str(IP_ADRRESS) + '/update/'
    # Tests to see if we already have an API Key
    try:
        if os.stat("API_KEY.txt").st_size > 0:
            # If we do, lets use it
            fileReader = open("API_KEY.txt")
            apiKey = fileReader.read()
            fileReader.close()
        else:
            # If not, lets get user to create one
            apiKey = authenticate()
    except:
        apiKey = authenticate()
    return apiKey

def startLogging(targetFile):
    fileWriter = open(targetFile, 'r+')    # overwrite previous log file
    fileWriter.truncate(0)
    return fileWriter

def recordStream(apiKey, fileWriter):
    # Opens a new HTTP session that we can use to terminate firehose onto
    sessionObj = requests.Session()
    sessionObj.headers = {'X-API-Key': apiKey}
    sessionReader = sessionObj.get(
        'https://partners.dnaspaces.io/api/partners/v1/firehose/events', stream=True)  # Change this to .io if needed
    # Jumps through every new event we have through firehose
    print("Starting Stream")
    for line in sessionReader.iter_lines():
        if line:
            # decodes payload into useable format
            decoded_line = line.decode('utf-8')
            event = json.loads(decoded_line)
            # writes every event to the logs.json in readible format
            fileWriter.write(str(json.dumps(json.loads(line), indent=4, sort_keys=True)))    
            # gets the event type out the JSON event and prints to screen
            eventType = event['eventType']
            print(eventType)
            



# #############################################################################
# Main Workflow
# #############################################################################
apiKey = establishConnection()
fileWriter = startLogging(targetFile="logs.json")
recordStream(apiKey, fileWriter)