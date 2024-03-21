# #############################################################################
# Project:   Submission to START Hackathon 2024 - Cisco Challenge
# Team:      BembelEngineers
# Authors:   Kevin Riehl, Leon Bernard, Benedikt Völker
# Date:      March 21st, 2024
# #############################################################################




# #############################################################################
# Imports
# #############################################################################
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import PIL.Image
from typing import Set, List, Iterable




# #############################################################################
# Methods
# #############################################################################
def convertToStrTimestamp(intTime):
    return datetime.utcfromtimestamp(int(intTime)).strftime('%Y-%m-%d %H:%M:%S')

def getDistanceEuclid(x1, y1, x2, y2):
    return np.linalg.norm(np.asarray([x1, y1]) - np.asarray([x2, y2]))

def render_gif_animation(lst_image_files: List[str], target_file: str, speed:int=100, first_last_slow:bool=True):
    """
    This function reads static images from a list of image files, and stores 
    all of them in an GIF animation.
    
    Parameters
    ----------
    lst_image_files: List[str]
        A list with image files that shall be connected to a GIF animation.
    target_file : str
        The target file to store the GIF into.
    speed : int
        Optional, Defualt: 100. The time per image. The slower the faster the animation.
    first_last_slow : bool
        Optional, Default : True. This will repeat the first and the last 
        image for ten times, so the animation does not directly run.
        
    Returns
    -------
    None
    """
    frames = []
    if first_last_slow:
        for x in range(0,10):
            image = PIL.Image.open(lst_image_files[0])
            frames.append(image)
    for file in lst_image_files:
        image = PIL.Image.open(file)
        frames.append(image)
    if first_last_slow:
        for x in range(0,40):
            frames.append(frames[-1])
    frames[0].save(target_file, format='GIF',
                    append_images=frames[1:],
                    save_all=True,
                    duration=speed, loop=0)
    
plt.ioff()

# #############################################################################
# Main Workflow
# #############################################################################
# Load Data
timeline = pd.read_csv("timeline.csv")
del timeline['Unnamed: 0']

# Parameters
N_USERS = 10
distanceThreshold = 0.1

# Determine Users
userIDs = timeline["userID"].tolist()
selected_individuals = userIDs[0:N_USERS]
usercolors = ["red", "darkorange", "chartreuse", "darkgreen", "lightseagreen", "dodgerblue", "navy", "blueviolet", "purple", "fuchsia"]

# Generate Movement Noise
noiseLVL = 1
noisesX = [np.random.normal(0, noiseLVL, size=timeline[timeline["userID"]==user].shape[0]) for user in selected_individuals]
noisesY = [np.random.normal(0, noiseLVL, size=timeline[timeline["userID"]==user].shape[0]) for user in selected_individuals]
positionsX = [timeline[timeline["userID"]==user]["x"] for user in selected_individuals]
positionsY = [timeline[timeline["userID"]==user]["y"] for user in selected_individuals]
positionsT = [timeline[timeline["userID"]==user]["timestampSec"] for user in selected_individuals]

allTimes = []
for t in positionsT:
    for t2 in t:
        allTimes.append(t2)
beginTime = min(allTimes)
endTime = max(allTimes)

adjacencyMatrix = np.zeros((N_USERS,N_USERS))
    
for time in range(beginTime, endTime+1, 1):
    print(time, endTime)
    timeIdxs = []
    for userIdx in range(0,N_USERS):
        try:
            timeIdx = next(x for x, val in enumerate(positionsT[userIdx]) if val >= time)
            timeIdxs.append(timeIdx)
        except:
            timeIdxs.append(-1)
        
    for userIdx1 in range(0,N_USERS):
        for userIdx2 in range(0,N_USERS):
            if userIdx1 != userIdx2:
                if timeIdxs[userIdx1]!=-1 and timeIdxs[userIdx2]!=-1:
                    x1 = positionsX[userIdx1].iloc[timeIdxs[userIdx1]]
                    x2 = positionsX[userIdx2].iloc[timeIdxs[userIdx2]]
                    y1 = positionsY[userIdx1].iloc[timeIdxs[userIdx1]]
                    y2 = positionsY[userIdx2].iloc[timeIdxs[userIdx2]]
                    if getDistanceEuclid(x1, y1, x2, y2) <= distanceThreshold:
                        adjacencyMatrix[userIdx1][userIdx2] += 1
                
    # Generate Figure per Time
    plt.figure(figsize=(14,6))
    plt.suptitle("Social Graph Generation [Time t="+convertToStrTimestamp(time)+"¨]", fontweight="bold")
    
    plt.subplot(1,2,1)
    plt.title("Employee Trajectories")
    for userIdx in range(0,N_USERS):
        idx = timeIdxs[userIdx]
        if idx!=-1:
            userDF = timeline[timeline["userID"]==userIDs[userIdx]]
            userDF = userDF.iloc[0:idx+1]
            noizX = noisesX[userIdx][0:idx+1]
            noizY = noisesY[userIdx][0:idx+1]
            xx = userDF["x"]+noizX
            yy = userDF["y"]+noizY
            xx = xx.reset_index()
            yy = yy.reset_index()
            del xx["index"]
            del yy["index"]
            alphas = np.zeros(yy.shape[0])
            if len(xx)>1:
                if beginTime-time > 10:
                    alphas[-10:] = 1
                for it in range(0, len(xx)-1):
                    if it > len(xx)-10:
                        al = 1.0
                    else:
                        al = 0.2
                    plt.plot([xx["x"].iloc[it], xx["x"].iloc[it+1]], [yy["y"].iloc[it], yy["y"].iloc[it+1]], color=usercolors[userIdx], alpha=al)
            plt.scatter(xx["x"].iloc[-1], yy["y"].iloc[-1], color=usercolors[userIdx], label="Employee "+str(userIdx+1))
        else:
            userDF = timeline[timeline["userID"]==userIDs[userIdx]]
            noizX = noisesX[userIdx]
            noizY = noisesY[userIdx]
            xx = userDF["x"]+noizX
            yy = userDF["y"]+noizY
            plt.plot(xx, yy, label="Employee "+str(userIdx+1), color=usercolors[userIdx])
            plt.scatter(xx.iloc[-1], yy.iloc[-1], color=usercolors[userIdx])

    plt.legend(loc="lower left")
    plt.xlabel("Position [x]")
    plt.ylabel("Position [y]")
    plt.xlim([45, 300])
    plt.ylim([24, 180])
    
    plt.subplot(1,2,2)
    plt.title("Time spent together [sec]")# "Social Network Graph Adjacency Matrix")
    plt.xlabel("Employee i")
    plt.ylabel("Employee j")
    plt.gca().set_xticks(np.arange(0,10))
    plt.gca().set_yticks(np.arange(0,10))
    plt.gca().set_xticklabels([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    plt.gca().set_yticklabels([" ", " ", " ", " ", " ", " ", " ", " ", " ", " "])
    for userIdx in range(0,N_USERS):
        plt.text(-0.9, userIdx, str(userIdx+1), fontweight="bold", color=usercolors[userIdx])
    for userIdx in range(0,N_USERS):
        plt.text(userIdx-0.1, 10, str(userIdx+1), fontweight="bold", color=usercolors[userIdx])
    plt.imshow(adjacencyMatrix, cmap="plasma")
    plt.colorbar()
    
    plt.tight_layout()
    plt.savefig("anim/Fig_"+str(time)+".png", dpi=100)
    plt.close()

np.savetxt("adjacencyMatrix.csv", adjacencyMatrix, delimiter=",")

imgFileList = []
for time in range(beginTime, endTime+1, 1):
    imgFileList.append("anim/Fig_"+str(time)+".png")
render_gif_animation(imgFileList, target_file="animation.gif", speed=100, first_last_slow=False)