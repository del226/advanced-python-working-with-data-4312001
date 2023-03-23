# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import datetime


with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD
def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig

sigquakes = sorted(data["features"], key=getsig,reverse=True)
sigquakes= sigquakes[:40]
sigquakes.sort(key=lambda e: e["properties"]["time"], reverse=True)
header = ["Magnitude", "Place", "Felt Reports", "Significance", "Link", "Date"]
rows = []

for quake in sigquakes:
    thedate = datetime.date.fromtimestamp(
            int(quake["properties"]["time"]/1000))
    rows.append([quake["properties"]["mag"],
                 quake["properties"]["place"],
                 0 if quake["properties"]["felt"] is None else quake["properties"]["felt"],
                 quake["properties"]["sig"],
                 quake["properties"]["url"],
                 thedate])
with open("sigquakes.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)
