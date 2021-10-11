from SensorReader import *
import requests
from datetime import datetime

URL = "https://hometempapi.azurewebsites.net/values"


while True:
    try:
        temp, hum = return_values()
        now = datetime.now()
        date = now.strftime("%Y-%m-%dT%H:%M:%S")
        print("date: {}, temp: {}, hum: {}".format(date, temp, hum))
        # data = {"date":"","temperature":temp, "humidity":hum}
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(5)
        continue
    except Exception as error:
        sensor.exit()
        continue
    time.sleep(5)