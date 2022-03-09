class Store:
    def __init__(self,name,list):
        self.name = name
        self.list = list

    def add_product(self, new_product):
        self.list['product'].append(new_product)
    
    def sell_product(self,id):
        pass

    def inflation(self,percent_increase):
        pass

    def set_clearance(self,category,percent_discount):
        pass
        

class Product:
    def __init__(self,name,price,product):
        self.name = name
        self.price = price
        self.product = product
 
    def update_price(self,percent_change,is_increased):
        