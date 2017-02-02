from sense_hat import SenseHat

sense = SenseHat()

While True:
  north = sense.get_compass()
  print("North: %s" % north)
  # alternatives
  print(sense.compass)
