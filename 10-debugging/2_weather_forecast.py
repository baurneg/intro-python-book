# Our predict_weather function should output a message indicating whether a sunny 
# or cloudy day lies ahead. However, the output is the same every time the function 
# is invoked. Why? Fix the code so that it behaves as expected.

# Copy Code
import random

def predict_weather(sunshine):
    if sunshine:
        return ("Today's weather will be sunny!")
    else:
        return ("Today's weather will be cloudy!")

sunshine = random.choice([True, False])
print(predict_weather(sunshine))