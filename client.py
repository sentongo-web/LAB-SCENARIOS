# ## Test and Validate

# Import the RemoteRunnable class from the langserve library
from langserve import RemoteRunnable


# Define the LangServe URL
url = "http://localhost:8000/weather"

# Invoke the endpoint of the LangServe for Temperature
data = {
    "weather_property": "temperature",
    "weather_description": "Today is sunny, making it a perfect day to spend outdoors with clear skies and bright sunshine. As you step outside, you might feel a gentle breeze adding to the pleasant atmosphere. With temperatures reaching a comfortable 75 degrees Fahrenheit, it is an ideal time for outdoor activities or simply relaxing in the sun. Although the humidity is 25%, it can get a rainfall of 20mm daily."
}

openai = RemoteRunnable(url)
openai.invoke(data)


# Invoke the endpoint of the LangServe for Humidity
data = {
    "weather_property": "humidity",
    "weather_description": "Today is sunny, making it a perfect day to spend outdoors with clear skies and bright sunshine. As you step outside, you might feel a gentle breeze adding to the pleasant atmosphere. With temperatures reaching a comfortable 75 degrees Fahrenheit, it is an ideal time for outdoor activities or simply relaxing in the sun. Although the humidity is 25%, it can get a rainfall of 20mm daily."
}

openai = RemoteRunnable(url)
openai.invoke(data)
