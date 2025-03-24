# PartB.py  # B1. File created with this name

import unittest
from PartA import Vehicle, Car  # Import classes from PartA.py

class TestObjectInstances(unittest.TestCase):
    # B2. Test if an object is an instance of a class.
    def test_vehicle_instance(self):
        vehicle = Vehicle("Test Model", 2000, 100, 5000, "blue")
        self.assertIsInstance(vehicle, Vehicle)

    # B3. Test if an object is NOT an instance of a class.
    def test_not_car_instance(self):
        vehicle = Vehicle("Test Model", 2000, 100, 5000, "blue")
        # Vehicle is not an instance of Car
        self.assertNotIsInstance(vehicle, Car)

    # B4. Test if two objects are identical (i.e., refer to the same object).
    def test_object_identity(self):
        vehicle = Vehicle("Test Model", 2000, 100, 5000, "blue")
        same_vehicle = vehicle
        self.assertIs(vehicle, same_vehicle)

class TestUpdateMethods(unittest.TestCase):
    # B5. Unit tests to verify that update methods work correctly for Vehicle.
    def test_vehicle_update_methods(self):
        vehicle = Vehicle("Test Model", 2000, 100, 5000, "blue")
        # Correct update should change the attribute.
        vehicle.set_model("Updated Model")
        self.assertEqual(vehicle.model, "Updated Model")
        
        vehicle.set_manufacture_year(2010)
        self.assertEqual(vehicle.manufacture_year, 2010)
        
        vehicle.set_top_speed(120)
        self.assertEqual(vehicle.top_speed, 120)
        
        vehicle.set_distance(6000)
        self.assertEqual(vehicle.distance, 6000)
        
        vehicle.set_color("red")
        self.assertEqual(vehicle.color, "red")
        
        # Incorrect update: should not change the attribute (remains the previous correct value)
        vehicle.set_manufacture_year("Not an int")
        self.assertEqual(vehicle.manufacture_year, 2010)

    # B5. Unit tests to verify that update methods work correctly for Car.
    def test_car_update_methods(self):
        car = Car("Test Car", 2018, 120, 30000, "green", "petrol", 4)
        # Correct update for extra attributes.
        car.set_fuel_type("diesel")
        self.assertEqual(car.fuel_type, "diesel")
        
        car.set_door_count(2)
        self.assertEqual(car.door_count, 2)
        
        # Incorrect update: attribute should remain unchanged.
        car.set_fuel_type(123)
        self.assertEqual(car.fuel_type, "diesel")
        
        car.set_door_count("two")
        self.assertEqual(car.door_count, 2)

# B6. Main function to run all the tests.
if __name__ == '__main__':
    unittest.main()

    
