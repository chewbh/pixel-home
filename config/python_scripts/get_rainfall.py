#!/usr/bin/python3

import sys
from requests import get

def get_rainfall_by_station(station_id):
  # query rainfall data from NEA
  response = get("https://api.data.gov.sg/v1/environment/rainfall").json()
  readings = response['items'][0]['readings']
  stations = response['metadata']['stations']
  reading_unit = response['metadata']['reading_unit']
  return [reading for reading in readings if reading['station_id'] == station_id][0]['value']


# S220 is sengkang
station_id = sys.argv[1]

print(get_rainfall_by_station(station_id))

