from sense_hat import SenseHat

sense = SenseHat()

while True:  
  north = sense.get_compass()
  print("North: %s" % north)
  # alternatives
  print(sense.compass)
