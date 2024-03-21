
![HackLogo](banner.png "HackLogo")

# Socialiser - connect people in companies

## A submission by team "BembelEngineers" to START Hack 2024 - CISCO Challenge

Team "BembelEngineers" from TU Darmstadt and ETH Zürich.
Members: Kevin Riehl, Leon Bernard, Benedikt Völker

We present "Socialiser", a recommender system that brings people together in companies.
Based on WiFi-Localisation data, we learn a social network graph, that is analysed to identify gaps in corporate network structure and actively suggests informal meetings for exchange and getting together.

## How it works
- Event Stream Data from CISCO Spaces is produced.
- This Stream Data is transmitted via Firehose API to our first software module "Graph Generator".
- The "Graph Generator" translates the event stream data into a social network graph (either real time or ex-post).
- The social graph yields insights for management to define company goals.
- The company goals together with the social graph are the input for the software module "Recommender System".
- The "Recommender Software" generates meeting suggestions to actively connect people to achieve company goals.
- The meeting suggestions are then sent via the WebEx Messaging Bot API to chats of the peopl in the company.
- These meeting suggestions lead to real meetings and thus serve the company goals.

![System Structure](Structure.PNG "System Structure")

![Animation](animation.gif "Animation")

The calculated centralities and a possible recommendation:
```
katz_centrality = [0.29344988 0.29344988 0.32605542 0.2974038  0.2974038  0.33809951 0.34483903 0.32605542 0.29344988 0.34483903]
degree_centrality = [0.         0.         0.66538462 0.08846154 0.08846154 0.86153846 1.         0.66538462 0.         1.        ]

influential_node = 6
isolated_node = 0
recommended_meeting = [influential_node, isolated_node]
```

## Structure of this repository
In this repository you will find three software modules.
- Folder "graphGenerator" contains a Python project that processes StreamData from CISCO Spaces via Firehose API, and generates the social network graph.
- Folder "recommederSystem" contains a Python project that analyses the social network graph and generates meeting recommendations.
- Folder "webexAPI" contains a NodeJS project that enables to send meeting invites automatically via a WebexChat Bot.


## Exemplary Code Workflow
```
# Record Stream Data
apiKey = establishConnection()
fileWriter = startLogging(targetFile="logs.json")
recordStream(apiKey, fileWriter)

# Filter Stream Data
fullStream = loadData(targetFile="logs.json")
filteredStream = filterStreamData(fullStream)

# Convert To User-Timeline
timelineDF = generateTimeLine(filteredStream2)

# Calculate Social Network Graph
graph_matrix = generateGraph(timelineDF)

# Hier kommt DEIN PART
```
