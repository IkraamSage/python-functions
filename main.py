#   exercise 1

def distance_from_zero(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return "nope!"


#   compulsory task
#   Define a function called hotel_cost with one argument nights as input.


def hotel_costs(nights):
    return 140*nights

#   define function called plane_ride


def plane_ride_cost(city):
    if "Cape Town" == city:
        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800

#   define a function called rental_car_cost


def rental_car_cost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days


def new_sum(*numbers):
    return new_sum(numbers)


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_costs(days) + plane_ride_cost(city) + spending_money


print(trip_cost("JHB", 5, 10))
