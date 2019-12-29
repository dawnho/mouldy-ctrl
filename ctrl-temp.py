#!/usr/bin/env python

import os, re, requests

SENSOR_IP = os.getenv("SENSOR_IP", "10.0.28.81")
TEMP_THRESHOLD = os.getenv("TEMP_THRESHOLD", "24.0")
SENSOR_LABELS = {
  "temperature": "nodemcu_temperature_celsius",
  "airpressure": "nodemcu_airpressure_hectopascal",
  "airpressure_sea": "nodemcu_airpressure_sealevel_hectopascal",
  "humidity": "nodemcu_humidity_percent",
  "dewpoint": "nodemcu_dewpoint_celsius"
}
def main():
    r = requests.get("http://mouldy.cutelab.house/")
    data_array = r.text.split('\n')
    temp_match = "^{} (.+)".format(SENSOR_LABELS["temperature"])
    temp_reading = next(re.match(temp_match, x).groups()[0] for x in data_array if re.match(temp_match, x))

    if temp_reading is None:
        return False

    if float(temp_reading) < float(TEMP_THRESHOLD):
      print("Turning Heater On")
      os.system("./tplink_smartplug.py -t {} -c on".format(SENSOR_IP))
    else:
      print("Turning Heater On")
      os.system("./tplink_smartplug.py -t {} -c off".format(SENSOR_IP))

main()
