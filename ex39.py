import sys

# Let's do some examples on using dictionaries
states = {  'New York':'NY',
            'California':'CA',
            'Michigan':'MI',
            'Oregon':'OR',
            'Florida':'FL'}

cities = {  'CA':'San Fransisco',
            'MI':'Detroit',
            'FL':'Jacksonville'}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Printing some cities
print('-'*50)
print('NY state has', cities['NY'], 'city')
print('OR state has', cities['OR'], 'city')

# Printing some states
print('-'*50)
print('Michigan\'s abbreviation is ',states['Michigan'])
print('California\'s abbreviation is ', states['California'])

# Doing the dictionary from the dictionary type
print('-'*50)
print("Michigan has ", cities[states['Michigan']], "city")
print("California has ", cities[states['California']],"city")

# Printing every abbreviation
print('-'*50)
for i in states.keys():
    print(f"The abbreviation of {i} is", states[i])

# Printing every city in state
print('-'*50)
for i in states.keys():
    print(f"State {i} has", cities[states[i]], "city")

# Now both city and abbreviation at a time
print('-'*50)
for i in states.keys():
    print("The abbreviation of {i} state is", states[i])
    print("State {i} has", cities[states[i]], "city")

# Now safely get abbreviation of the state that is not included in the dictionary safely
print('-'*50)
state = states.get('Texas')

if state is None:
    print("Sorry, No Texas ! You should probably append it")

# Get the cities by default value
city = cities.get('TX', 'Doesnt exist')
print(f"The city for the state 'TX' is: {city}")