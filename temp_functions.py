"""
# this is the function that converts Fahrenheit temperature to Celsius temperature.
input °F and then return °C
"""
def fahr_to_celsius(temp_fahrenheit):
  converted_temp = (temp_fahrenheit - 32) / 1.8
  return converted_temp
# ------------------------
"""
This is the function that classifier temprature in Celsius into 4(0-3) based on above criteria.
"""
def temp_classifier(temp_celsius):
  if temp_celsius < -2: # check from the most strict one.
    return 0
  elif temp_celsius < 2:
    return 1
  elif temp_celsius < 15:
    return 2
  else:
    return 3

