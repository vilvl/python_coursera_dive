class Value:
    
    def __init__(self):
        self.amount = 0

    def __get__(self, obj, obj_type):
        return self.amount    
    
    def __set__(self, obj, value):
        diff = (value - self.amount)
        if diff <= 0:
            self.amount = value
        else:
            self.amount = self.amount + diff * (1 - obj.commission)
    
    def __delete__(self, obj, obj_type):
        pass
        
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission
    
    def add_amount(self, value):
        self.amount = self.amount + value
