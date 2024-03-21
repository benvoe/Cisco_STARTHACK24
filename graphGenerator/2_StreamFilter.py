# #############################################################################
# Project:   Submission to START Hackathon 2024 - Cisco Challenge
# Team:      BembelEngineers
# Authors:   Kevin Riehl, Leon Bernard, Benedikt Völker
# Date:      March 21st, 2024
# #############################################################################




# #############################################################################
# Imports
# #############################################################################
import json
from datetime import datetime
import numpy as np
import pandas as pd




# #############################################################################
# Methods
# #############################################################################
def loadData(targetFile):
    fileReader = open(targetFile, "r")
    fullStreamTXT = fileReader.read()
    fileReader.close()
    fullStreamTXT = "["+fullStreamTXT.replace("}{","},{")+"]"
    fullStream = json.loads(fullStreamTXT)
    return fullStream

def determineEventTypesAndCounts(fullStream):
    eventTypes = []
    for entry in fullStream:
        if not entry["eventType"] in eventTypes:
            eventTypes.append(entry["eventType"])
    eventCounter = {}
    for evType in eventTypes:
        eventCounter[evType] = 0
    for entry in fullStream:
        eventCounter[entry["eventType"]] += 1
    return eventCounter

def determineDeviceTypes(filteredStream):
    deviceTypes = []
    for entry in filteredStream:
        if not entry["iotTelemetry"]["deviceInfo"]["deviceType"] in deviceTypes:
            deviceTypes.append(entry["iotTelemetry"]["deviceInfo"]["deviceType"])
    deviceCounter = {}
    for dvType in deviceTypes:
        deviceCounter[dvType] = 0
    for entry in filteredStream:
        deviceCounter[entry["iotTelemetry"]["deviceInfo"]["deviceType"]] += 1
    return deviceCounter

def filterStreamData(fullStream):
    # 1. Filter Event Type, "IOT_TELEMETRY"
    filter_eventType = "IOT_TELEMETRY"
    filteredStream = []
    for entry in fullStream:
        if entry["eventType"]==filter_eventType:
            filteredStream.append(entry)
    deviceCounter = determineDeviceTypes(filteredStream)
    
    # 2. Filter  Device Type, "IOT_BLE_DEVICE" / This is actually not user smartphone
    filter_eventType = "IOT_BLE_DEVICE"
    filteredStream2 = []
    for entry in filteredStream:
        if entry["iotTelemetry"]["deviceInfo"]["deviceType"]==filter_eventType:
            filteredStream2.append(entry)
        
    return filteredStream2, deviceCounter

def generateTimeLine(filteredStream2):
    # 3. Get Unique Device IDs
    userIDs = []
    for entry in filteredStream2:
        if not entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"] in userIDs:
            userIDs.append(entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"])
            
    # Create TimeLines
    timeLine = []
    for entry in filteredStream2:
        userID = entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"]
        positionLat = entry["iotTelemetry"]["detectedPosition"]["latitude"]
        positionLon = entry["iotTelemetry"]["detectedPosition"]["longitude"]
        positionX = entry["iotTelemetry"]["detectedPosition"]["xPos"]
        positionY = entry["iotTelemetry"]["detectedPosition"]["yPos"]
        timestampSec = str(entry["recordTimestamp"])[:-3] # in seconds not milliseconds
        timestamp = datetime.utcfromtimestamp(int(timestampSec)).strftime('%Y-%m-%d %H:%M:%S')
        timeLine.append([userID, timestamp, timestampSec, positionLat, positionLon, positionX, positionY])
    timelineDF = pd.DataFrame(timeLine, columns=["userID", "timestamp", "timestampSec", "latitude", "longitude", "x", "y"])
    timelineDF.to_csv("timeline.csv")
    
    return timelineDF

# #############################################################################
# Main Workflow
# #############################################################################
fullStream = loadData(targetFile="logs.json")
eventCounter = determineEventTypesAndCounts(fullStream)

# 1. Filter Event Type, "IOT_TELEMETRY"
filter_eventType = "IOT_TELEMETRY"
filteredStream = []
for entry in fullStream:
    if entry["eventType"]==filter_eventType:
        filteredStream.append(entry)
deviceCounter = determineDeviceTypes(filteredStream)

# 2. Filter  Device Type, "IOT_BLE_DEVICE" / This is actually not user smartphone
filter_eventType = "IOT_BLE_DEVICE"
filteredStream2 = []
for entry in filteredStream:
    if entry["iotTelemetry"]["deviceInfo"]["deviceType"]==filter_eventType:
        filteredStream2.append(entry)

# 3. Get Unique Device IDs
userIDs = []
for entry in filteredStream2:
    if not entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"] in userIDs:
        userIDs.append(entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"])
        
# Create TimeLines
timeLine = []
for entry in filteredStream2:
    userID = entry["iotTelemetry"]["deviceInfo"]["deviceMacAddress"]
    positionLat = entry["iotTelemetry"]["detectedPosition"]["latitude"]
    positionLon = entry["iotTelemetry"]["detectedPosition"]["longitude"]
    positionX = entry["iotTelemetry"]["detectedPosition"]["xPos"]
    positionY = entry["iotTelemetry"]["detectedPosition"]["yPos"]
    timestampSec = str(entry["recordTimestamp"])[:-3] # in seconds not milliseconds
    timestamp = datetime.utcfromtimestamp(int(timestampSec)).strftime('%Y-%m-%d %H:%M:%S')
    timeLine.append([userID, timestamp, timestampSec, positionLat, positionLon, positionX, positionY])
timelineDF = pd.DataFrame(timeLine, columns=["userID", "timestamp", "timestampSec", "latitude", "longitude", "x", "y"])
timelineDF.to_csv("timeline.csv")