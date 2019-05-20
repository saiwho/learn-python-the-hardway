# Initialize the integer variable cars with 100
cars = 100

# Initialize the float variable space_in_car with 4.0
space_in_car = 4

# Initialize the integer variable drivers with 30
drivers = 30

# Initialize the integer variable passengers with 100
passengers = 90

# No of cars driven = No of drivers available; So cars_not_driven is given below
cars_not_driven = cars - drivers

# No of cars driven = No of drivers
cars_driven = drivers

#Total drivable cars space
car_pool_capacity = space_in_car*cars_driven

#avg passengers per car = total driven cars/toal passengers
average_passengers_per_car = passengers/cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", car_pool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
"in each car.")
