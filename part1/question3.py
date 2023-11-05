################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

class Oven:
  """
  This class is for a magical oven that can combine ingredients at
  different temperatures to craft special materials.

  Attributes:
    ingredients (list): A list of ingredients.
    temperature (str): The temperature of the oven. Can be "frozen", "boiled", or "waiting".
  
  Methods:
    add(item): Adds an item to the oven.
    freeze(): Sets the temperature of the oven to "frozen".
    boil(): Sets the temperature of the oven to "boiled".
    wait(): Sets the temperature of the oven to "waiting".
    get_output(): Returns the result material based on ingredients and temperature.
  """
  def __init__(self) -> None:
    self.ingredients = []
    self.temperature = ""

  def add(self, item) -> None:
    """
    Adds an item to the oven.

    Args:
      item: An item to be added to the oven.
    """
    self.ingredients.append(item)

  def freeze(self) -> None:
    """
    Sets the temperature of the oven to "frozen".
    """
    self.temperature = "frozen"
    
  def boil(self) -> None:
    """
    Sets the temperature of the oven to "boiled".
    """
    self.temperature = "boiled"

  def wait(self) -> None:
    """
    Sets the temperature of the oven to "waiting".
    """
    self.temperature = "waiting"

  def get_output(self) -> str:
    """
    Returns the result material based on ingredients and temperature.

    Returns:
      str: The result material based on ingredients and temperature.
    """
    if self.temperature == "frozen" and "water" in self.ingredients and "air" in self.ingredients:
        return "snow"
    elif self.temperature == "boiled" and "lead" in self.ingredients and "mercury" in self.ingredients:
        return "gold"
    elif self.temperature == "boiled" and "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
        return "pizza"
    else:
        return "unknown"
    

def make_oven():
  """
  Makes an oven instance.

  Returns:
    Oven: An oven instance.
  """
  return Oven()
    
def alchemy_combine(oven: Oven , ingredients : list  , temperature : int ) -> str :
  """
  Combines ingredients in an oven to make a new material.

  Args:
    oven (Oven): An oven instance.
    ingredients (list): A list of ingredients.
    temperature (int): The temperature of the oven.
  
  Returns:
    str: The name of the new material.
  """
  for item in ingredients:
    oven.add(item)
    
  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()