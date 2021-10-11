import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT22(board.D4, use_pulseio=False)

temp = 0
hum = 0

def return_values ():
        try:
            temp = sensor.temperature
            hum = sensor.humidity
            #print("Temp: {}, Humidity: {}".format(temp, hum)) 
            return temp, hum       
        except RuntimeError as error:
            print(error.args[0])
            pass
        except Exception as error:
            sensor.exit()
            raise error

        

