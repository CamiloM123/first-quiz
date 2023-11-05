from question1 import get_city_weather
import pytest

def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"

  assert get_city_weather("San Francisco") == "16 degrees and rainy"

  assert get_city_weather("Sao Paulo") == "17 degrees and cloudy"

def test_get_city_weather_nonexistent_city():
    with pytest.raises(KeyError):
        get_city_weather("Bogota")
