class Discount:
    
    def __init__(self,customer,price):
        self.customer = customer
        self.price = price
    
    def get_discount(self):
        if self.customer == 'normal':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4
        