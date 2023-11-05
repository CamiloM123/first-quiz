################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.

def get_city_temperature(city : str ) -> int :
   """
   Returns the temperature for a given city.

   Args: 
      city (str): The city name.
      
   Returns:
      int: The temperature in degrees Celsius.
   
   Raises:
      KeyError: If the city is not in the dictionary.
   """

   city_temperatures = {
      "Quito": 22,
      "Sao Paulo": 17,
      "San Francisco": 16,
      "New York": 14
   }

   temperature = city_temperatures[city]
   
   return temperature

def get_city_weather(city : str ) -> str :
   """
   Returns the weather for a given city.

   Args:
      city (str): The city name.
   
   Returns:
      str: The weather in the city.
   
   Raises:
      KeyError: If the city is not in the dictionary.
   """

   city_weather = {
      "Quito": "sunny",
      "Sao Paulo": "cloudy",
      "San Francisco": "rainy",
      "New York": "rainy"
   }
   
   sky_condition = city_weather[city]

   temperature = get_city_temperature(city)

   return f"{temperature} degrees and {sky_condition}"