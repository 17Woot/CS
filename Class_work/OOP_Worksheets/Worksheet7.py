class cars(object):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, Plate_number, Colour, Engine_size, price="none"):
        self.plate_number = Plate_number
        self.colour = Colour
        self.engine_size = Engine_size
        self.__price = price

    def start(self):
        return "Starting"

    def stop(self):
        return "Stopping"

    def accelerate(self):
        return "Accelerating"

    def set_price(self, p):
        self.__price = p

    def get_price(self):
        return self.__price



class sports_car(cars):
    def __init__(self, Plate_number, Colour, Engine_size, Top_speed):
        self.top_speed = Top_speed
        super().__init__(Plate_number, Colour, Engine_size, price="none")

    def accelerate(self):
        return "Accelerating 0-60 in 5 seconds"

    def brake(self):
        return "Braking, *smoke*"

    def drift(self):
        return "Drifting"

class convertible(cars):
    def __init__(self, Plate_number, Colour, Engine_size, Roof_status):
        self.roof_status = Roof_status
        super().__init__(Plate_number, Colour, Engine_size, price="none")

    def open_roof(self):
        return "Opening roof"

    def close_roof(self):
        return "Closing roof"

    def accelerate(self):
        return "Accelerating 0-60 in 12 seconds"

class estate(cars):
    def __init__(self, Plate_number, Colour, Engine_size, Boot_status):
        self.boot_status = Boot_status
        super().__init__(Plate_number, Colour, Engine_size, price="none")

    def open_boot(self):
        return "Opening boot"

    def carry_load(self):
        return "Carrying load"

    def accelerate(self):
        return "Accelerating 0-60 in 15 seconds"

if __name__ == "__main__":
    car_1 = sports_car("1234", "red", "3.2", "210")
    car_2 = convertible("5678", "blue", "2.0", "open")
    car_3 = estate("9012", "green", "1.6", "closed")
    print(car_1.accelerate())
    print(car_2.accelerate())
    print(car_3.accelerate())
    print(car_3.stop())
    print(car_3.open_boot())
    print(car_3.carry_load())
    print(car_3.start())






