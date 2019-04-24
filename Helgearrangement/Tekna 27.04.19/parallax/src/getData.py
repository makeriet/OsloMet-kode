import json

with open("trips-2018.6.1-2018.6.30.json", "r") as f:
  datastore = json.load(f)

trips = datastore["trips"]
destinations = {}

for trip in trips:
  if not trip["start_station_id"] in destinations:
    destinations[trip["start_station_id"]] = {trip["end_station_id"] : 1}
  else:
    if not trip["end_station_id"] in destinations[trip["start_station_id"]]:
      destinations[trip["start_station_id"]][trip["end_station_id"]] = 1
    else:
      destinations[trip["start_station_id"]][trip["end_station_id"]] += 1

with open('data.json', 'w') as outfile:  
    json.dump(destinations, outfile)