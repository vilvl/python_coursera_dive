import csv
from os.path import splitext
        

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.carrying = float(carrying)
        self.photo_file_name = photo_file_name
        if self.get_photo_file_ext() not in ('.jpg', '.jpeg', '.png', '.gif'):
            raise AttributeError
        
        
    def get_photo_file_ext(self):
    	return splitext(self.photo_file_name)[-1]
        

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            self.body_length, self.body_width, self.body_height = \
             map(lambda x: float(x), body_whl.split('x'))
        except Exception:
            self.body_length, self.body_width, self.body_height = 0., 0., 0.
        
    def get_body_volume(self):
    	return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем 
        for row in reader:
            try:
                
                car_type, brand, passenger_seats_count, photo_file_name, body_whl, carrying, extra = row
                if car_type == 'car' and all((brand, photo_file_name, carrying, passenger_seats_count)):
                    car_list.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                elif car_type == 'truck' and all((brand, photo_file_name, carrying)):
                    car_list.append(Truck(brand, photo_file_name, carrying, body_whl))
                elif car_type == 'spec_machine' and all((brand, photo_file_name, carrying, extra)):
                    car_list.append(SpecMachine(brand, photo_file_name, carrying, extra))
            except Exception:
                continue
    return car_list
    
    
        
