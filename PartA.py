# PartA.py   # A1. File named as required

# A2. Define the base class representing a Vehicle with the given attributes.
class Vehicle:
    def __init__(self, model, manufacture_year, top_speed, distance, color):
        self.model = model                  # Expected type: str
        self.manufacture_year = manufacture_year  # Expected type: int
        self.top_speed = top_speed          # Expected type: int/float
        self.distance = distance            # Expected type: int/float
        self.color = color                  # Expected type: str

    # A3. Method to display all the attributes.
    def show_specs(self):
        print("Vehicle Specifications:")
        print("Model            :", self.model)
        print("Manufacture Year :", self.manufacture_year)
        print("Top Speed        :", self.top_speed)
        print("Distance Driven  :", self.distance)
        print("Color            :", self.color)
        print("-" * 30)

    # A4. Methods to update each attribute with basic type validation.
    def set_model(self, new_model):
        if isinstance(new_model, str):
            self.model = new_model
        else:
            print("Error: 'model' must be a string.")

    def set_manufacture_year(self, new_year):
        if isinstance(new_year, int):
            self.manufacture_year = new_year
        else:
            print("Error: 'manufacture_year' must be an integer.")

    def set_top_speed(self, new_speed):
        if isinstance(new_speed, (int, float)):
            self.top_speed = new_speed
        else:
            print("Error: 'top_speed' must be numeric.")

    def set_distance(self, new_distance):
        if isinstance(new_distance, (int, float)):
            self.distance = new_distance
        else:
            print("Error: 'distance' must be numeric.")

    def set_color(self, new_color):
        if isinstance(new_color, str):
            self.color = new_color
        else:
            print("Error: 'color' must be a string.")


# A5. Define a subclass of Vehicle (Car) with additional attributes.
class Car(Vehicle):
    def __init__(self, model, manufacture_year, top_speed, distance, color, fuel_type, door_count):
        super().__init__(model, manufacture_year, top_speed, distance, color)
        self.fuel_type = fuel_type    # Expected type: str (e.g., 'petrol', 'diesel')
        self.door_count = door_count  # Expected type: int

    # A6. Overridden method to display both base and additional attributes.
    def show_specs(self):
        super().show_specs()  # Display Vehicle specifications
        print("Fuel Type  :", self.fuel_type)
        print("Door Count :", self.door_count)
        print("=" * 30)

    # A7. Methods to update the extra attributes with type checks.
    def set_fuel_type(self, new_fuel_type):
        if isinstance(new_fuel_type, str):
            self.fuel_type = new_fuel_type
        else:
            print("Error: 'fuel_type' must be a string.")

    def set_door_count(self, new_door_count):
        if isinstance(new_door_count, int):
            self.door_count = new_door_count
        else:
            print("Error: 'door_count' must be an integer.")


# A8. Create instances with proper initial values.
if __name__ == "__main__":
    # Create an instance of Vehicle.
    auto = Vehicle("Toyota Corolla", 2010, 120, 50000, "red")
    
    # A9. Display the attributes using the show_specs method.
    print("Initial Vehicle Details:")
    auto.show_specs()
    
    # A10. Demonstrate updates to the Vehicle instance.
    # Correct updates:
    auto.set_model("Toyota Camry")
    auto.set_manufacture_year(2015)
    auto.set_top_speed(130)
    auto.set_distance(45000)
    auto.set_color("blue")
    # Incorrect updates to trigger type validation:
    auto.set_manufacture_year("Two Thousand Fifteen")
    auto.set_top_speed("fast")
    
    print("Updated Vehicle Details:")
    auto.show_specs()

    # Create an instance of Car (child class).
    my_car = Car("Honda Civic", 2018, 130, 30000, "blue", "petrol", 4)
    
    # A9. Display the Car details.
    print("Initial Car Details:")
    my_car.show_specs()
    
    # A10. Update Car-specific attributes.
    # Correct updates:
    my_car.set_fuel_type("diesel")
    my_car.set_door_count(2)
    # Incorrect updates:
    my_car.set_fuel_type(123)
    my_car.set_door_count("two")
    
    print("Updated Car Details:")
    my_car.show_specs()
