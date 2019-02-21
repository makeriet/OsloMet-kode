
# coding=utf-8
import json
import requests
from identifier import *

#printer ut en JSON med en liste over alle stasjonene til Oslo bysykkel med
#tilhørende data
stations = requests.get('https://oslobysykkel.no/api/v1/stations', headers = {'Client-Identifier': API_key})
parsed_stations = json.loads(stations.text)

with open("stasjoner.JSON","w") as f:
	jrg = json.dumps(parsed_stations, f, indent=4)
	f.write(jrg)
	print(jrg)
	f.close()
