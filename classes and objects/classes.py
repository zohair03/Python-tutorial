class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print(f"moves away...")

    def move_forward(self):
        print(f"{self.make} {self.model} is moving forward..")
    
    def move_backward(self):
        print(f"{self.make} {self.model} is moving backward..")

    def move_left(self):
        print(f"{self.make} {self.model} is taking left turn..")

    def move_right(self):
        print(f"{self.make} {self.model} is taking right turn..")

    def apply_brake(self):
        print(f"{self.make} {self.model} is stoped..")



class Car(Vehicle):
    pass

class Bike(Vehicle):
    def moves(self):
        print(f"Rides away...")

class Golfcart(Vehicle):
    pass

class Truck(Vehicle):
    def moves(self):
        print(f"Rummbles away...")

class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print(f"Flies away..., and has faa_id:{self.faa_id}")


my_car = Car('Mercedes', 'GLA C200')
my_bike = Bike('bike', 'suzukii')
my_golfcart = Golfcart('Mercedes', 'GLA C200')
my_truck = Truck('Mercedes', 'GLA C200')
my_airplane = Airplane('luftansa', 'Boeing 747', "F-837272")



for v in (my_car, my_bike, my_golfcart, my_truck, my_airplane):
    v.moves()
    v.move_forward()
    v.move_left()
    v.move_forward()
    v.move_right()
    v.move_forward()
    v.apply_brake()







# my_car = Vehicle('Mercedes', 'GLA C200')

# my_car.move_forward()
# my_car.move_left()
# my_car.move_forward()
# my_car.move_right()
# my_car.move_forward()
# my_car.apply_brake()


# your_car = Vehicle('BMW', 'Gost')

# your_car.move_forward()
# your_car.move_left()
# your_car.move_forward()
# your_car.move_right()
# your_car.move_forward()
# your_car.apply_brake()

