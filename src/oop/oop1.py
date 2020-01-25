# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#


class Vehicle:  # base
    pass


class GroundVehicle(Vehicle):
    pass


class Car (GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle(Vehicle):
    pass


class Airplane(FlightVehicle):
    pass


class Starship(FlightVehicle):
    pass
