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


# #############################################################################
# Methods
# #############################################################################




# #############################################################################
# Main Workflow
# #############################################################################
timeline = pd.read_csv("timeline.csv")
del timeline['Unnamed: 0']
noiseLVL = 1

selected_individuals = []

for n in range(0,10):
    user = timeline["userID"].iloc[n]
    userDF = timeline[timeline["userID"]==user]
    plt.plot(userDF["x"]+np.random.normal(0, noiseLVL, size=userDF.shape[0]), userDF["y"]+np.random.normal(0, noiseLVL, size=userDF.shape[0]), label="Indivudal "+str(n))
plt.legend()