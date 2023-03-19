# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

#1. How many quakes in total?
print("Total quakes: "+str(data["metadata"]["count"]))


# 2: How many quakes were felt by at least 100 people?
def filterhundred(x):
    f = x["properties"]["felt"]
    return f is not None and f >=100
filtered = list(filter(filterhundred, data["features"]))
print("Total quakes >=100: "+str(len(filtered)))


# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
def getppl(x):
    ppl = x["properties"]["felt"]
    if ppl is None:
        return 0
    return ppl
maxReport = max(data["features"], key = getppl)
print("Max Report: "+str(maxReport["properties"]["title"])+" with "+str(maxReport["properties"]["felt"])+" reports")

# 4: Print the top 10 most significant events, with the significance value of eachi
def getsig(x):
    sig = x["properties"]["sig"]
    if sig is None:
        return 0
    return sig
sortQuake = sorted(data["features"], key=getsig, reverse=True)
print("Top 10 significant events")
for i in range(0,10):
    event = sortQuake[i]["properties"]
    print("Event: "+event["title"]+"\t\tsignificance: "+str(event["sig"]))
