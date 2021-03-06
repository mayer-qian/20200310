class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.make
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        self.odometer_reading += mileage

    def fill_gas_tank(self):
        print("I have gas_tank")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 10
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.update_odometer(100)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

    #def describe_battery(self):
        #print("This car has a " + str(self.battery_size) + "-kwh battery")

    def fill_gas_tank(self):
        print("I have not gas_tank")


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")


my_tesla = ElectricCar('tesla', 'model S', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.fill_gas_tank()
