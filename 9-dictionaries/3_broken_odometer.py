# Broken Odometer
# Using the following code, delete the 'mileage' 
# key and its associated value from car.

# Copy Code
# car = {
#     'type':    'sedan',
#     'color':   'blue',
#     'mileage': 80_000,
#     'year':    2003,
# }
car = {
    'type':    'sedan',
    'color':   'blue',
    'mileage': 80_000,
    'year': 2003
}

del car['mileage']
print(car)