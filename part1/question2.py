################################################################################
#     ____                          __     _                          ___ 
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__ \
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         __/ /
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / __/ 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/ 
#                                                                         
#  Question 2
################################################################################
#
# Instructions:
# Write a function that will swap a tuple of two items. For example, the function 
# should change (x, y) into (y, x). 
# Assign the function to `swapper` so that the function `run_swapper(..)` can use
# it. As always, there is a test suite that checks the result. It is in 
# `question2_test.py.`

swapper = None

def swapper(tuple_item : tuple) -> tuple:
  """
  Swaps the items in a tuple.  

  Args:
    tuple_item (tuple): A tuple of two items.

  Returns:
    tuple: A tuple of two items. The items are swapped.
  """
  #Time Complexity: O(n)
  #Auxiliary Space: O(n)
  list_item = list(tuple_item)
  list_item.reverse()   
  
  return tuple(list_item)
  

def run_swapper(list_of_tuples : list) -> list:
  """
  Runs the swapper function on a list of tuples. 

  Args:
    list_of_tuples (list): A list of tuples.

  Returns:
    list: A list of tuples. Each tuple has two items.
  """
  return list(map(swapper, list_of_tuples))

