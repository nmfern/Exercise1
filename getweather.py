from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import os

owm = OWM(os.environ['OWM_API_KEY'])
mgr = owm.weather_manager()

observation = mgr.weather_at_place(os.environ['OWM_CITY'])
w = observation.weather

print("The following details:" + w.detailed_status)
print("Humidity: ",w.humidity)
print("Temperature: ",w.temperature('celsius'))
print("Heat: ",w.heat_index)
print("Clouds: ",w.clouds)
